<template>
  <div class="relative  group border rounded inline-block text-left w-[150px]">
    <div class="border px-4 py-2 rounded bg-white shadow-md cursor-pointer text-center">
      {{Hover_name}}
    </div>

    <div class="absolute left-0 w-full z-10 border shadow-md hidden group-hover:block bg-white">
      <ul>
        <li
         v-for="option in list_options" :key="option"
        @click="Chooes( option)" :class="['px-4 py-2  cursor-pointer hover:bg-gray-200',  Selected.includes(option)? 'text-red-600': '']">{{option}}</li>

      </ul>
    </div>
  </div>


</template>

<script setup>
import {ref} from 'vue'

const props = defineProps ({
  list_options: {
    type: Array,
  },
  Hover_name: {
    type: String,
    
  },
  phrase: {
    type: String
  },
  initial:{
    type: Array
  }
})

const Selected = ref(props.initial)
const emit = defineEmits(['Send_list'])

 


const Chooes = (option) => {
    if (!Selected.value.includes(option)) {
       Selected.value.push(option)
    } 
    else {
        Selected.value = Selected.value.filter(item => item != option)
    }
    // console.log(initial.value)
    console.log(props.Hover_name)
    emit('Send_list', Selected.value)

}


</script>
