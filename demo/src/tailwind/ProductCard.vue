<template>
  <div class="max-w-sm bg-white rounded-lg shadow-md overflow-hidden flex flex-col items-center p-4 gap-4 md:flex-row md:max-w-2xl">
    <!-- Hình ảnh sản phẩm -->
    <img
      :src="image"
      alt="Sản phẩm"
      class="w-[225px] h-[225px] object-cover rounded-md"
    />

    <!-- Thông tin sản phẩm -->
    <div class="flex flex-col justify-between gap-3 text-center md:text-left">
      <h2 class="text-xl font-semibold">{{ name }}</h2>
      <p class="text-gray-700">{{ description }}</p>
      <p class="text-green-600 font-bold">{{ price }}</p>

      <button
        class="mt-2 bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
      >
        Mua ngay
      </button>
    </div>
  </div>
</template>

<script setup>
defineProps({
  name: String,
  price: String,
  description: String,
  image: String
})
</script>
