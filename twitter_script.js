const tweetUser = 'UserID'

const querySelectorHas = function( parent, child ){
  return [].filter.call( document.querySelectorAll( parent ), function( elem ){
    if(elem.querySelector( child ) !== null ) {
      return true        
    }
    else {
      return false
    }
  });
}


const querySelectorInner = function( parent, inner ){
  return [].filter.call( document.querySelectorAll( parent ), function( elem ){
    if(elem.innerHTML == inner ) {
      return true
    }
    else {
      return false
    }
  });
}



setInterval(() => {

  console.log('--- Twitter Removal Script ---')


  var amountUnretweets = 0
  for (const d of document.querySelectorAll('div[data-testid="unretweet"]')) {
    amountUnretweets++
    d.click()
  }
  var amountUnretweetconfirms = 0
  for (const r of document.querySelectorAll('div[data-testid="unretweetConfirm"]')) {
    amountUnretweetconfirms++
    r.click()
  }
  console.log('Unretweets: ' + amountUnretweets + ', Confirms: ' + amountUnretweetconfirms)


  var amountClicks = 0
  for(const d of querySelectorHas("div[data-testid='tweet']", "a[href='/" + tweetUser + "']")) {
   const moreButton = d.querySelector("div[aria-label='More']")
   amountClicks++
   moreButton.click()
  }
  var amountClickDeletes = 0
  for(const deleteButton of querySelectorInner("span", 'Delete')) {
    deleteButton.click()
    amountClickDeletes++
  }
  var amountClickConfirms = 0
  for(const deleteConfirm of document.querySelectorAll("div[data-testid='confirmationSheetConfirm']")) {
    deleteConfirm.click()
    amountClickConfirms++
  }
  console.log('Menu: ' + amountClicks + ', Deletes: ' + amountClickDeletes + ', Confirms: ' + amountClickConfirms)

  window.scrollTo(0, document.body.scrollHeight)

}, 3000) // Run every 3s
