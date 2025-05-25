

<template>
 <div class="w-full mt-6">
  
    <h2 class="ml-10 w-full text-blue-800 text-3xl mb-5">1. OPTION YOU CHOOSE</h2>
   <div class="flex gap-3 bg-blue-300 p-5 mx-auto w-full justify-center">
      <div  class="" v-for="item in default_introduction" :key="item.key">
        <Drop_down
        :Hover_name='item.key'
        :phrase="item.introduction_phrace"
        :list_options="item.options"
        :initial="item.UserChoices"
        @Send_list="(data) => UpdataData(data, item.key)"
        />
  
      </div>
   </div>

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
 </div>
</template>


<script setup>
import Drop_down from './Drop_down.vue';
import {ref} from 'vue'

const default_introduction = ref([
  {
    key: 'Job',
    introduction_phrace: 'I am',
    options: ['Software Engineer', 'Student', 'Accountant', 'Teacher', 'Doctor', 'Salesperson', 'Office Staff', 'Factory Worker'],
    UserChoices: ['Software Engineer', 'Student', 'Teacher']
  },
  {
    key: 'Hobby',
    introduction_phrace: 'I enjoy',
    options: ['reading novels', 'playing football', 'painting landscapes', 'listening to music', 'cooking for my family'],
    UserChoices: ['reading novels', 'listening to music']
  },
  {
    key: 'Personality',
    introduction_phrace: 'People often describe me as',
    options: ['hardworking', 'friendly', 'curious', 'creative', 'reliable'],
    UserChoices: ['friendly', 'creative']
  },
  {
    key: 'Future goal',
    introduction_phrace: 'In the future, I want to',
    options: ['start my own business', 'travel the world', 'become a team leader', 'study abroad', 'work in a global company'],
    UserChoices: ['travel the world', 'study abroad']
  },
  {
    key: 'Excellent skills',
    introduction_phrace: 'I am good at',
    options: ['solving problems', 'communicating with people', 'managing time', 'learning new things quickly', 'using design tools like Figma'],
    UserChoices: ['solving problems', 'learning new things quickly']
  },
  {
    key: 'Education',
    introduction_phrace: 'I studied at',
    options: ['High School', 'College', 'University', 'Master', 'PhD'],
    UserChoices: ['High School']
  }
]);



const UpdataData = (data, targetkey) => {
  console.log(data)

  const item = default_introduction.value.find(i => i.key === targetkey)
  if (item) {
  item.UserChoices = [...data] // hoặc = data nếu bạn chắc chắn đã là mảng mới
}


}

</script>


    <div class="w-full relative  p-3">
      <button class="absolute left-5 border">Confirm to change</button>
    </div>


<template>
  <div class="p-4">
     <h2 class="ml-10 w-full text-blue-800 text-3xl mb-5">2. CHOOSE TOPICS</h2>
    <ul class="grid grid-cols-5 gap-y-6 text-center ">
      <li v-for="topic in topics.daily_conversation_topics " :key="topic"
      :class="['border shadow-xl w-30 hover:scale-110 rounded-4xl flex items-center justify-center' , topics.userChoises.includes(topic)? 'bg-blue-500' : 'bg-gray-200']"
      @click="toggleChoice(topic)"
      >
        {{topic}}
      </li>
    </ul>
  </div>
</template>


<script setup>
import {ref} from 'vue'

const topics = ref({
  daily_conversation_topics  : [
    "weather",
    "work or school",
    "family",
    "hobbies and interests",
    "food and cooking",
    "movies or TV shows",
    "weekend plans",
    "health and fitness",
    "travel",
    "news and current events"
], 
  userChoises : [
     "hobbies and interests",
    "food and cooking",
    "movies or TV shows",
    "weekend plans",
  ]
})


const toggleChoice = (topic) => {
  if (topics.value.userChoises.includes(topic)) {
    topics.value.userChoises = topics.value.userChoises.filter(item => item !== topic)
  } else 
  {
    topics.value.userChoises.push(topic)
  }
  console.log(topics.value.userChoises.includes(topic), topic)
}


</script>