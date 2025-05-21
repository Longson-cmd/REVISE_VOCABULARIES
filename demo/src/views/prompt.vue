<template>
  <div class="flex-1 w-full h-full flex flex-col justify-center">
    <div class="flex w-[850px] h-1/2 p-4 mx-auto">
      <button @click="pickRandom" class="mr-4 h-10 px-4 bg-blue-500 text-white rounded hover:bg-blue-600 flex-shrink-0">New prompt</button>
      <div class="relative flex-1 bg-white rounded-lg p-4 font-mono overflow-auto text-sm shadow-md border border-gray-200 ">
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
          class="w-full bg-transparent resize-none outline-none overflow-hidden"
          rows="8"
        />
      </div>
    </div>
  
    <div class="p-4 w-[850px] h-1/2 mx-auto bg-white  rounded">
      <!-- Input and button -->
      <div class="flex gap-2 mb-4">
        <input
          type="text"
          v-model="sentence"
          placeholder="Enter your sentence"
          class="flex-1 border border-gray-300 rounded px-2 py-1 text-3xl"
        />
        <button
          @click="add_sentence"
          class="bg-blue-500 text-white px-4 rounded hover:bg-blue-600"
        >
          Add
        </button>
      </div>
  
      <!-- Show sentence and speaker icon -->
      <div v-if="show_sentence" class="flex items-center justify-between gap-2 bg-gray-100 p-2 rounded">
        <span class="text-3xl text-red-600">{{ submittedSentence }}</span>
        <i class="fas fa-volume-up text-blue-500 cursor-pointer" @click="playAudio"></i>
      </div>
    </div> 
  </div>

</template>

<script setup>

import axios from 'axios'
import { ref, onMounted , nextTick} from 'vue'


const show_sentence = ref(false)
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
    show_sentence.value = false
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



// ADD sentences Component
const sentence = ref('')
const word = ref('')

const submittedSentence = ref('')
let audio = null
const add_sentence = async() => { 
    const text = sentence.value.trim()
    if (!text) return
    word.value = 'eat'
    try {    
        await axios.put('http://127.0.0.1:5000/words', {
        word: randomword.value, 
        sentence : text
        })
        submittedSentence.value = text
        sentence.value = ''
        show_sentence.value = true
        console.log('Added sentence!')
    } catch(e) {
        console.error('there is an error' + e)
    }
}

function safeFilename(sentence) {
  return sentence
    .replace(/[^\w\s]/g, '')   // remove punctuation
    .replace(/\s+/g, '_')      // replace spaces with _
    + '.mp3'
}

const playAudio = (audioPath) => {
    const filename = safeFilename(submittedSentence.value)
    audio = new Audio(`http://localhost:5000/backend/audios/sentences/${filename}`)
    console.log(`http://localhost:5000/backend/audios/sentences/${filename}`)
    try {
        audio.play()
    } catch(e) {
        console.error('Audio play failed:', e)
    }
}



</script>
