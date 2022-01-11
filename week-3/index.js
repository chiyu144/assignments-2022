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
          loadMoreBtn.disabled = true ,
          loadMoreBtn.textContent = '沒有景點囉 !',
          loadMoreBtn.style.cursor = 'unset'
        ) : nextPage ++
      } 
    })
  } else {
    const loadingSpinner = document.querySelector('.loading-spinner')
    loadingSpinner.style.display = 'none'
    const notFound = document.createElement('div')
    notFound.textContent = '查無資料'
    overlayBox.appendChild(notFound)
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
    onImgLoaded(img)
    const div = document.createElement('div')
    div.classList.add('article-title')
    div.textContent = `${stitle}`
    article.appendChild(img)
    article.appendChild(div)
    fragment.appendChild(article)
  })

  mainSection.appendChild(fragment)
}

// * 實作 Skeleton 用
// * 整個流程: fetch 資料 → loading spinner 畫面 → 資料回來等圖片載入中 → Skeleton 畫面 → 圖片載好 → 正常畫面)
const onImgLoaded = img => {
  if (img.complete) {
    // * 圖片已被載入 (圖片無情瞬間載好，不需做事)
    return
  } else {
    // * 如果圖片還沒載好，顯示 Skeleton
    img.classList.add('skeleton')
    // * 圖片載好後，關掉 Skeleton
    img.onload = () => img.classList.remove('skeleton')
  }
}
