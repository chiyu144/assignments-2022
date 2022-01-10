const apiUrl = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
let nextPage = 2
const pageUnit = 8

document.addEventListener('DOMContentLoaded', async () => {
  const articles = await getArticles(apiUrl)
  const overlayBox = document.querySelector('.overlay-box')
  
  if (articles?.length > 0) {
    overlayBox.style.display = 'none'
    renderArticles(articles)
    const loadMoreBtn = document.querySelector('#load-more-btn')
    loadMoreBtn.style.display = 'inline-block'
    loadMoreBtn.addEventListener('click', () => {
      if (loadMoreBtn.textContent === '沒有景點囉 !') return
      else {
        renderArticles(articles, nextPage)
        articles.length / pageUnit <= nextPage
        ? (
          loadMoreBtn.textContent = '沒有景點囉 !',
          loadMoreBtn.disabled = true 
        ) : nextPage ++
      } 
    })
  } else {
    const loadingSpinner = document.querySelector('.loading-spinner')
    loadingSpinner.style.display = 'none'
    const notFount = document.createElement('div')
    notFount.textContent = '查無資料'
    overlayBox.appendChild(notFount)
  } 
});

const getArticles = async (apiUrl) => {
  try {
    const { result } = await fetch(`${apiUrl}`).then(data => data.json())
    return result.results
  } catch (e) {
    console.warn(`Error Message: ${e}`)
  }
}

const renderArticles = (articles, nextPage = 1) => {
  const mainSection = document.querySelector('#main-section')
  const fragment = document.createDocumentFragment()

  const startIndex = nextPage === 1 ? 0 : (nextPage - 1) * pageUnit
  const endIndex = pageUnit * nextPage

  articles.slice(startIndex, endIndex).forEach(({ stitle, file }) => {
    const article = document.createElement('article')
    const img = document.createElement('img')
    img.src = file.split('https://').map(val => 'https://' + val).slice(1)[0]
    const div = document.createElement('div')
    div.className = 'article-title'
    div.textContent = `${stitle}`
    article.appendChild(img)
    article.appendChild(div)
    fragment.appendChild(article)
  })

  mainSection.appendChild(fragment)
}