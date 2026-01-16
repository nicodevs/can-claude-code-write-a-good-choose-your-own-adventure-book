#!/usr/bin/env node
import { readFileSync } from 'fs'
import { intro, outro, select, note, cancel, isCancel, confirm } from '@clack/prompts'

function loadOutline(filePath) {
  try {
    const content = readFileSync(filePath, 'utf8')
    return JSON.parse(content)
  } catch (error) {
    console.error(`Error loading outline: ${error.message}`)
    process.exit(1)
  }
}

function formatText(text) {
  // Replace [BREAK] with newlines for better readability
  return text.replace(/\s*\[BREAK\]\s*/g, '\n\n')
}

function getEndingMessage(endType) {
  const endings = {
    BEST: '🌟 BEST ENDING - Congratulations! You achieved the best possible outcome!',
    GOOD: '✨ GOOD ENDING - Well done! You reached a positive conclusion.',
    NEUTRAL: '📖 NEUTRAL ENDING - The story concludes, but the journey continues...',
    BAD: '💔 BAD ENDING - Things did not go as hoped.',
    DEATH: '💀 DEATH - Your adventure has come to an untimely end.'
  }
  return endings[endType] || `📖 THE END (${endType})`
}

async function playNode(node, depth = 0) {
  // Display the story text
  console.log('\n' + '─'.repeat(60) + '\n')
  console.log(formatText(node.text))
  console.log('\n' + '─'.repeat(60))

  // Check if this is an ending
  if (node.end) {
    console.log('\n' + getEndingMessage(node.end) + '\n')
    return true
  }

  // Check if there are choices
  if (!node.choices || Object.keys(node.choices).length === 0) {
    console.log('\n📖 THE END\n')
    return true
  }

  // Build options from choices
  const choiceEntries = Object.entries(node.choices)
  const options = choiceEntries.map(([choiceText, childNode], index) => ({
    value: index,
    label: choiceText,
    hint: childNode.end ? `(${childNode.end} ending)` : undefined
  }))

  // Ask user to make a choice
  const selection = await select({
    message: 'What do you do?',
    options
  })

  if (isCancel(selection)) {
    cancel('Adventure abandoned.')
    process.exit(0)
  }

  // Get the selected child node and continue
  const [, selectedNode] = choiceEntries[selection]
  return playNode(selectedNode, depth + 1)
}

async function main() {
  const args = process.argv.slice(2)

  if (args.length === 0) {
    console.error('Usage: node play.js <path-to-outline.json>')
    console.error('Example: node play.js ./input/outline.json')
    process.exit(1)
  }

  const outlinePath = args[0]
  const outline = loadOutline(outlinePath)

  intro('Choose Your Own Adventure')

  note(
    'Navigate through the story by selecting your choices.\nPress Ctrl+C at any time to quit.',
    'How to Play'
  )

  let playAgain = true

  while (playAgain) {
    await playNode(outline)

    playAgain = await confirm({
      message: 'Would you like to play again?',
      initialValue: false
    })

    if (isCancel(playAgain)) {
      playAgain = false
    }
  }

  outro('Thanks for playing!')
}

main().catch(console.error)
