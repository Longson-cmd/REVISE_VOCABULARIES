export const safeFilename = (text) => {
  return text
    .replace(/[^\w\s]/g, '')   // remove punctuation
    .replace(/\s+/g, '_')      // replace spaces with _
    + '.mp3'
}

export const playAudio = (sentenceText) => {
  const filename = safeFilename(sentenceText)
  const audio = new Audio(`http://localhost:5000/backend/audios/sentences/${filename}`)
  console.log(`http://localhost:5000/backend/audios/sentences/${filename}`)
  try {
    audio.play()
  } catch (e) {
    console.error('Audio play failed:', e)
  }
}
