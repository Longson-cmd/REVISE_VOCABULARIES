<template>
  <div class="p-6 space-y-6">
    <ProductCard
      name="Giày chạy bộ Nike"
      price="1.200.000đ"
      description="Thoáng khí, nhẹ nhàng, phong cách thể thao."
      image="/shoes.jpg"
    />

    <ProductCard
      name="Dép tổ ong cao cấp"
      price="99.000đ"
      description="Huyền thoại tuổi thơ, bền bỉ với thời gian."
      image="/slippers.jpg"
    />
  </div>
</template>

<script setup>
import ProductCard from './ProductCard.vue'

</script>
