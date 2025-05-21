<template>
    <div class="min-h-screen flex flex-col items-center l">
        <h1 class="text-5xl font-bold text-green-600 p-6 bg-blue-200 w-full shawdow-2xl text-center">List word</h1>

        <div class="flex justify-between w-full p-5 mb-5 bg-gray-100">
            <div>
                <input
                 type="text" 
                 placeholder="Enter new word"
                 class="border outline-none p-2 rounded-lg mr-3" 
                 v-model="new_word">
                <button class="bg-blue-600 p-2 rounded-sm hover:bg-blue-800 transition duration-300" @click="add_word">add</button>
            </div>
    
            <div class="flex flex-col ">
                <div class="flex gap-2 border px-2 rounded-lg">
                    <input
                    v-model="searchKey"
                    placeholder="Search word"
                    class="border p-2  w-full border-none outline-none"
                    />
                    <button @click="search_word(searchKey)" class="">
                        <i class="fas fa-search hover:text-[30px]"></i>
                    </button>
                </div>
                <span v-if="showMessage" class="text-red-600">There is no such word</span>
            </div>
        </div>


        <table class="p-10 table-auto border-collapse w-full text-center">
            <thead class="text-2xl font-semibold text-purple-600">
                <tr>
                    <th class="px-4 py-3">ID</th>
                    <th class="px-4 py-3">New word</th>
                    <th class="px-4 py-3">Notes</th>
                    <th class="px-4 py-3">Revise</th>
                
                    <th>Delete</th>
                </tr>
            </thead>

            <tbody class="text-2xl">
                <tr v-for="(word, index) in words" :key="index" 
                    @click="goToDetail(word.key)"
                    class="cursor-pointer hover:bg-gray-100"
                    >
                    <td class="px-4 py-3">{{index + 1}}</td>
                    <td class="px-4 py-3"> {{word.key}}</td>
                    <td class="px-4 py-3">--</td>
                    <td class="px-4 py-3"> {{word.number}}</td>
                    <td class="px-4 py-3">
                        <button class="flex justify-center w-full " @click.stop="Delete(word.key)">
                            <i class="fa fa-trash text-red-600 text-xl hover:text-3xl transition duration-100"></i>
                        </button>
                    </td>
                </tr>
                
            </tbody>

        </table>
    </div>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const words = ref([])
const router = useRouter()
const searchKey = ref('')
const list_words = ref([]) 
const new_word = ref('')

const fetch_data = async () => {
    try {
        const respone = await axios.get('http://127.0.0.1:5000/words')
        const initial_data = respone.data
        words.value = initial_data.reverse()
        list_words.value = words.value.map(item => item['key'])
        console.log(list_words.value)
        console.log('Data was fetched successfully')
    } catch(err) {
        console.error('there is an error in newwords.vue :', err)
    }
}

const add_word = async () => {
    try {
        const word = new_word.value.trim()
        if (!word) return
        await axios.post('http://127.0.0.1:5000/words', {word: word})
        console.log('add new word to json file')
        new_word.value = ''
        await fetch_data()
    } catch (err) {
        console.log('failed to add new word', err)
    }
}


const goToDetail = (key) => {
    router.push({name:'WordDetailPage', params: {key}})
}


onMounted(fetch_data)

const Delete = async (key) => {
    try {
        await axios.delete('http://127.0.0.1:5000/words', {data : {word: key}})
         await fetch_data ()
        console.log(`deleted ${key}`)
    } catch (err) {
        console.error (`Deleted ${key} has a error`)
    }
}


const showMessage = ref(false)
const search_word = (key) => {
    if (list_words.value.includes(key)) {
        goToDetail(key)
        console.log('this word is in list')
    }
    else {
        showMessage.value = true
        setTimeout(() => {
            showMessage.value = false
        }, 2000)
        searchKey.value = ''
        console.log('cant find this word')
    }
}

</script>