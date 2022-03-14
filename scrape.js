Array.from(document.querySelectorAll('.itemlist .athing')).map(el => {
  const title = el.querySelector('a.titlelink').innerText;
  const points = parseInt(el.nextSibling.querySelector('.score').innerText);
  const url = el.querySelector('a.titlelink').href;
  const dt = el.nextSibling.querySelector('.age').title;
  const submitter = el.nextSibling.querySelector('.hnuser').innerText;
  const commentsUrl = el.nextSibling.querySelector('.subtext a:last-child').href;
  const id = commentsUrl.split('?id=')[1];
  const numComments = parseInt(el.nextSibling.querySelectorAll('.subtext a[href^=item]')[0].innerText.split()[0]);
  return {id, title, url, dt, points, submitter, commentsUrl, numComments};
})
