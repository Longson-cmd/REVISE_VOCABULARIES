<template>
  <div class="p-6">
    <div class="mb-2 flex gap-2">
      <button @click="toggleEdit" class="bg-gray-300 px-3 py-1 rounded">
        {{ isEditing ? 'Save' : 'Edit' }}
      </button>
      <button @click="copyText" class="bg-green-400 px-3 py-1 rounded">
        Copy
      </button>
    </div>
    <textarea
      ref="textArea"
      v-model="text"
      :readonly="!isEditing"
      class="w-full border p-2 rounded"
      rows="5"
    />
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue'

const text = ref("This is an example text.")
const isEditing = ref(false)
const textArea = ref(null)


// textArea.value.focus() means:“Find the HTML element that has ref="textArea" and call .focus() on it.”
const toggleEdit = () => {
  isEditing.value = !isEditing.value
  if (isEditing.value) {
    nextTick(() => textArea.value.focus())
  }
}

const copyText = async () => {
  try {
    await navigator.clipboard.writeText(text.value)
    alert('Copied!')
  } catch (e) {
    console.error(e)
  }
}
</script>
