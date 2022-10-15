Array.from(document.querySelectorAll('.itemlist .athing'), el => {
  const title = el.querySelector('.titleline a').innerText;
  const points = parseInt(el.nextSibling.querySelector('.score').innerText);
  const url = el.querySelector('.titleline a').href;
  const dt = el.nextSibling.querySelector('.age').title;
  const submitter = el.nextSibling.querySelector('.hnuser').innerText;
  const commentsUrl = el.nextSibling.querySelector('.age a').href;
  const id = commentsUrl.split('?id=')[1];
  // Only posts with comments have a comments link
  const commentsLink = Array.from(
    el.nextSibling.querySelectorAll('a')
  ).filter(el => el && el.innerText.includes('comment'))[0];
  let numComments = 0;
  if (commentsLink) {
    numComments = parseInt(commentsLink.innerText.split()[0]);
  }
  return {id, title, url, dt, points, submitter, commentsUrl, numComments};
})
