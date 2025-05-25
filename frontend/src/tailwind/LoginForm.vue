<template>
  <div class="flex items-center justify-center min-h-screen">
    <form
      @submit.prevent="handleSubmit"
      class="grid gap-4 w-full px-4 md:w-1/2 bg-white p-6 rounded-lg shadow-md"
    >
      <h2 class="text-2xl font-bold text-center">Đăng nhập</h2>

      <input
        type="email"
        v-model="email"
        placeholder="Email"
        class="border p-2 rounded w-full"
        required
      />

      <input
        type="password"
        v-model="password"
        placeholder="Mật khẩu"
        class="border p-2 rounded w-full"
        required
      />

      <button
        type="submit"
        class="bg-blue-600 text-white p-2 rounded hover:bg-blue-700 transition"
      >
        Đăng nhập
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const email = ref('')
const password = ref('')

const handleSubmit = () => {
  alert(`Email: ${email.value}, Mật khẩu: ${password.value}`)
}
</script>
