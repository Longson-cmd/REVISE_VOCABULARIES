<template>
  <div class="flex-1 items-start p-4">
    <button @click="pickRandom" class="mr-4 h-10 px-4 bg-blue-500 text-white rounded hover:bg-blue-600 flex-shrink-0">New prompt</button>
    <div class="relative bg-white rounded-lg p-4 font-mono text-sm shadow-md border border-gray-200 w-2/3">
      <div class="flex justify-between items-center mb-2">
        <span class="text-xs font-semibold text-gray-500">Prompt</span>
        <div class="flex space-x-3">
          <button @click="copyText" class="text-gray-600 hover:text-black" title="Copy">
            <i class="fas fa-copy"></i>
          </button>
          <button @click="toggleEdit" class="text-gray-600 hover:text-black" title="Edit">
            <i class="fas fa-edit"></i>
          </button>
        </div>
    </div>
  
      <textarea 
        ref="textArea"
        v-model="text"
        :readonly="!isEditing"
        class="w-full bg-transparent resize-none outline-none"
        rows="8"
      />
    </div>
  </div>


</template>

<script setup>
import axios from 'axios'
import { ref, onMounted , nextTick} from 'vue'


const words = ref([])
const keys = ref([])
const self = ref({})
const self_introduction = ref([])
const topics = ref([])
const randomSelf = ref('')
const randomTopic = ref('')
const randomword = ref('')

const text = ref('')
const isEditing = ref(false) // A reactive boolean that tracks whether the textarea is in editing mode
const textArea = ref(null)

const fetchWords = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:5000/words')
    words.value = response.data
    keys.value = words.value.filter(item => item.number > 3).map(item => item.key)
    console.log(keys.value)
    
    console.log('Data was fetched successfully')
  } catch (e) {
    alert('There is an error: ' + e.message)
  }


  try {
    const response = await axios.get('http://127.0.0.1:5000/self')
    self.value = response.data
    self_introduction.value = self.value.self_introduce
    // console.log('Topics fetched:', self.value.topics)
    topics.value = self.value.topics
    console.log('Data (self) was fetched successfully')
  } catch (e) {
    alert('There is an error (with self): ' + e.message)
  }
}

const pickRandom = () => {

    randomword.value = keys.value[Math.floor(Math.random() * keys.value.length)]
    randomSelf.value = self_introduction.value[Math.floor(Math.random() * self_introduction.value.length)]
    randomTopic.value = topics.value[Math.floor(Math.random() * topics.value.length)]
    // console.log(randomword.value)
    // console.log(randomSelf.value)
    // console.log(randomTopic.value)
    text.value = `I’m practicing English. Here is my self-introduction:
"${randomSelf.value}"

I'm focusing on the topic: "${randomTopic.value}"

Based on my self-introduction and this topic, please help me create a new sentence using the word "${randomword.value}".
Use simple language and express it in a natural way.`

}
onMounted(async () => {
  await fetchWords()
  pickRandom()


})


const toggleEdit = () => {
  isEditing.value = !isEditing.value

  if (isEditing.value) {
    nextTick(() => textArea.value.focus())
  }
}


// Function to copy the current text to clipboard
const copyText = async () => {
  try {
    await navigator.clipboard.writeText(text.value)
    alert('Copied to clipboard!')
  } catch (err) {
    console.error('Copy failed:', err)
  }
}
</script>
