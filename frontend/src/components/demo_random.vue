<template>
  <div class="p-6">
    <button @click="pickRandom" class="px-4 py-2 bg-blue-600 text-white rounded">New Prompt</button>
    <p class="mt-4 text-lg">{{ randomText }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const prompts = [
  "Tell me about your favorite food.",
  "Describe your dream job.",
  "What do you do in your free time?"
]

const randomText = ref('Click the button to get a prompt!')
// Math.random() Returns a random decimal number between 0 (inclusive) and 1 (exclusive)
// Math.floor(...) This rounds down to the nearest whole number

const pickRandom = () => {
  const index = Math.floor(Math.random() * prompts.length)
  randomText.value = prompts[index]
}
</script>


<!-- Day 1 – Practice: Basic Random Prompt Generator
Day 2 – Practice: Copy to Clipboard & Toggle Editable Text
Day 3 – Practice: Fetch Data with axios -->