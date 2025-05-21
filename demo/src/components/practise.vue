<template>
  <div class="relative group border rounded inline-block">
    <div>
      Hover to chooes
    </div>

    <div class="absolute left-0 w-full z-10 hidden group-hover:block bg-white">
      <ul v-for="option in list_1" :key="option">
        <li @click="Chooes(option)">{{option}}</li>

      </ul>
    </div>
  </div>

  <p>you chosed: {{Selected}}</p>
</template>

<script setup>
import {ref} from 'vue'

const list_1 = ['a', 'b', 'c']

const Selected = ref('none')

const Chooes = (option) => {
  Selected.value = option
}
</script>
