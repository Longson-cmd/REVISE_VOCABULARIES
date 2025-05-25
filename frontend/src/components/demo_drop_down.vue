<!-- group (on parent): Marks the parent element as a hover group.
group-hover:block (on child): When the parent .group is hovered, show this element as block. -->
<template>
  <div class="relative inline-block text-left group">
    <!-- Button + Dropdown wrapper -->
    <div class="border px-4 py-2 rounded bg-white shadow-md cursor-pointer">
      Hover to choose
    </div>

    <!-- Dropdown: no gap and full width -->
    <div class="absolute left-0 w-full bg-white border shadow-md rounded z-10 hidden group-hover:block">
      <ul class="flex flex-col">
        <li
          class="px-4 py-2 hover:bg-gray-100 cursor-pointer"
          @click="selectOption('Option 1')"
        >
          Option 1
        </li>
        <li
          class="px-4 py-2 hover:bg-gray-100 cursor-pointer"
          @click="selectOption('Option 2')"
        >
          Option 2
        </li>
      </ul>
    </div>
  </div>

  <!-- Show selected option -->
  <p class="mt-4 text-lg">Selected: {{ selected }}</p>
</template>

<script setup>
import { ref } from 'vue';
const selected = ref('None');
const selectOption = (option) => {
  selected.value = option;
};
</script>
