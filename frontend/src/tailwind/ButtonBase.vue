<template>
  <button
    :class="[
      'px-6 py-2 rounded text-white transition duration-300',
      bgColor,
      hoverEffect
    ]"
  >
    <slot />
  </button>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  bgColor: {
    type: String,
    default: 'bg-blue-600',
  },
  hoverEffect: {
    type: String,
    default: 'hover:bg-green-600 hover:scale-105',
  },
})
</script>
