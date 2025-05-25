

<template>
 <div class="w-full  mb-[100px]">
    <h1 class="text-5xl text-center p-8 bg-blue-200 font-bold ">PERSONALIZE & CHOOSE TOPIC</h1>

    <!-- Part 1 -->
    <h2 class="ml-10 w-full text-blue-800 text-3xl my-5">I. SELF INTRODUCTION</h2>  
    <h3 class="ml-15 w-full text-yellow-600 text-2xl mb-5">1. BY DEFAULT</h3>
    <!--Five  Drop_downs -->
   <div class="flex gap-3 bg-blue-300 p-5 mx-auto w-full justify-center">
      <div  class="" v-for="item in default_introduction" :key="item.key">
        <Drop_down
        :Hover_name='item.key'
        :phrase="item.introduction_phrace"
        :list_options="item.options"
        :initial="item.UserChoices"
        @Send_list="(data) => UpdateData(data, item.key)"
        />
  
      </div>
   </div>

    <div class="w-full p-5 mb-10 relative">
      <button class="absolute right-5 border p-1 bg-purple-600 text-white rounded-xl px-3 hover:scale-120"
      @click="updata_self"
      >
        Confirm to change
      </button>
    </div>

   
    <!-- show imformation of drop down -->
    <div class="grid grid-cols-3 gap-5 bg-gray-100 p-3">
      <div class="" v-for="item in default_introduction" :key="item.key">
        <ul class="list-disc pl-10 space-y-3">
          <div class="text-red-600 ml-10 text-xl font-semibold py-3 w-full">{{item.key}}</div>
          <li v-for="option in item.UserChoices" :key="option" class="border-b border-gray-300 ">
            {{item.introduction_phrace}} <strong>{{option}}</strong>
          </li>
        </ul>
      </div>
    </div>


    <!-- users add more information -->
    <h3 class="ml-15 w-full text-yellow-600 text-2xl my-5">2. ADD MORE</h3>
    <ul class="flex flex-col gap-3 bg-gray-100 py-5 text-2xl">
      <li v-for="sentence in self_introduce" :key="sentence"
      class="list-disc ml-20"
      >
        {{sentence}}
        <button @click="delete_sentence(sentence)">
          <i class="fas fa-trash"></i>
        </button>
      </li>
    </ul>
  <div class="flex py-8 justify-center gap-3">
      <input type="text" v-model="sentence" class="border w-2/3 p-2 shadow-2xs focus:outline-none" placeholder="Tell us more about yourself">
      <button class="p-2 bg-blue-400 rounded-sm text-white font-semibold" @click="add_sentence">ADD</button>
  </div>

    <div class="w-full p-5 mb-10 relative">
      <button class="absolute right-5 border p-1 bg-purple-600 text-white rounded-xl px-3 hover:scale-120"
      @click="updata_self"
      >
        Confirm to change
      </button>
    </div>


    <h2 class="ml-10 text-blue-800 text-3xl mb-5">II. CHOOSE TOPICS</h2>
    <ul class="w-full grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-y-6  text-center px-20 pb-10 mx-auto">
      <li v-for="topic in topics.daily_conversation_topics " :key="topic"
      :class="['border shadow-xl w-30 hover:scale-110 rounded-4xl flex items-center justify-center' , topics.userChoises.includes(topic)? 'bg-blue-500' : 'bg-gray-200']"
      @click="toggleChoice(topic)"
      >
        {{topic}}
      </li>
    </ul>
      <div class="w-full p-5 mb-10 relative">
      <button class="absolute right-5 border p-1 bg-purple-600 text-white rounded-xl px-3 hover:scale-120"
      @click="updata_self"
      >
        Confirm to change
      </button>
    </div>

 </div>

</template>


<script setup>
import Drop_down from './Drop_down.vue';
import {ref, onMounted} from 'vue'
import axios from 'axios';

// DECLARE VARIABLE
const default_introduction = ref([])
const self_introduce = ref([])
const topics = ref([])

const sentence = ref('')

// fetch data
const fetch_data = async () => {
  try {
      const response = await axios.get('http://127.0.0.1:5000/self')
      default_introduction.value = response.data.default_introduction
      self_introduce.value = response.data.self_introduce
      topics.value = response.data.topics
      console.log('fetch data sucessfully!')
  } catch(err) {
    console.log('There is an error', err)
  }
}
    

// INTRODUCTION PART
// by default
const UpdateData = (data, targetkey) => {
  console.log(data)

  const item = default_introduction.value.find(i => i.key === targetkey)
  if (item) {
  item.UserChoices = [...data] // hoặc = data nếu bạn chắc chắn đã là mảng mới
}
}
// add more imformation
const delete_sentence = (sentence) => {
  self_introduce.value = self_introduce.value.filter(item => item != sentence)
}

const add_sentence = () => {
  const text = sentence.value.trim()
  if (!text) return 

  self_introduce.value.push(text)
  sentence.value = ''

}


// CHOOSE TOPICS
const toggleChoice = (topic) => {
  if (topics.value.userChoises.includes(topic)) {
    topics.value.userChoises = topics.value.userChoises.filter(item => item !== topic)
  } else 
  {
    topics.value.userChoises.push(topic)
  }
  console.log(topics.value.userChoises.includes(topic), topic)
}


const updata_self= async() => {

  const data = {
    "self_introduce":JSON.parse(JSON.stringify(self_introduce.value)),
    "default_introduction": JSON.parse(JSON.stringify(default_introduction.value)),
    "topics": JSON.parse(JSON.stringify(topics.value))
  }

  try {
    await axios.put('http://127.0.0.1:5000/self',data)
  } catch (err) {
    console.error('there is an error', err)
  }
  // console.log(data)

}
// JSON.stringify(...): This turns that array into a JSON string: "[{\"key\":\"Job\",\"introduction_phrace\":\"I am\",...}]"
// JSON.parse(...) This then turns that string back into a pure JavaScript object, free of Vue’s reactive system
onMounted(fetch_data)
</script>