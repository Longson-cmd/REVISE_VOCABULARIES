<template>
  <nav class="bg-blue-600 p-4">
    <div class="max-w-6xl mx-auto flex justify-between items-center">
      <!-- Logo -->
      <a href="/" class="text-white text-xl font-bold">Trang chủ</a>

      <!-- Hamburger Icon (Mobile) -->
      <button class="md:hidden text-white text-2xl" @click="isOpen = !isOpen">
        ☰
      </button>

      <!-- Desktop Links -->
      <div class="space-x-4 hidden md:flex">
        <a href="#about" class="text-white hover:text-gray-200">Giới thiệu</a>
        <a href="#services" class="text-white hover:text-gray-200">Dịch vụ</a>
        <a href="#contact" class="text-white hover:text-gray-200">Liên hệ</a>
      </div>
    </div>

    <!-- Mobile Links -->
    <div v-if="isOpen" class="md:hidden mt-2 space-y-2">
      <a href="#about" class="block text-white hover:text-gray-200">Giới thiệu</a>
      <a href="#services" class="block text-white hover:text-gray-200">Dịch vụ</a>
      <a href="#contact" class="block text-white hover:text-gray-200">Liên hệ</a>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'

const isOpen = ref(false)
</script>
