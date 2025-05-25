<template>
  <div class="min-h-screen flex flex-col font-sans">

    <!-- Header -->
    <header class="bg-blue-600 text-white text-xl text-center p-5">
      Learning English with Specific Topic
    </header>

    <!-- Hero -->
    <div class="bg-blue-50 text-center text-xl font-bold p-10">
      Pray Budda this script doesn't have bugs
    </div >

    <!-- Container -->
    <div class="flex flex-1">
      
      <!-- Sidebar -->
      <aside class="w-[250px] bg-gray-100 boder-r border-gray-300 p-5 flex flex-col justify-between">
        <div>
          <!-- stronger than normal but lighter than bold). -->
          <h3 class="mb-2 font-semibold">Menu</h3>
          <!-- You can click anywhere in the row, not just the text. -->
        
    
          <RouterLink to="/NewWords" class="block text-blue-600 mb-1 hover:underline">New words</RouterLink>
          <RouterLink to="/self_introduction" class="block text-blue-600 mb-1 hover:underline">About you</RouterLink>
        </div>
        
        <div class="pt-5 flex gap-3 justify-center">
          <a href="#" class="bg-green-600 hover:bg-green-700 text-white py-2 px-4 rounded">Contact</a>
          <a href="#" class="bg-green-600 hover:bg-green-700 text-white py-2 px-4 rounded">Sign Up</a>
        </div>
      </aside>

      <!-- Main Content -->
      <main class="flex-1 flex flex-col items-start m-0" >
          <prompt/>
      </main>
    </div>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white text-center p-4">
      &copy; 2025 Learning English. Follow us:
      <a href="#" class="text-blue-400 mx-2 hover:underline">Facebook</a> |
      <a href="#"  class="text-blue-400 mx-2 hover:underline">Zalo</a>
    </footer>

  </div>
</template>
  
<script setup>

import Prompt from './prompt.vue';

</script>