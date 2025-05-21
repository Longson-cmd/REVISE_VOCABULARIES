<template>
  <div class="flex gap-4 justify-center items-center min-h-screen">
    <BaseButton>Click Me</BaseButton>
    <BaseButton bgColor="bg-red-600" hoverEffect="hover:bg-yellow-500 hover:scale-110">
      Delete
    </BaseButton>
  </div>
</template>

<script setup>
import BaseButton from './BaseButton.vue'
</script>
