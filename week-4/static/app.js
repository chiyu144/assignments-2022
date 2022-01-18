const postSignIn = async ({ userId, password }) => {
  try {
    const res = await fetch(`/signin`, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({userId, password})
    });
    return res;
  } catch (err) {
    console.warn(err);
  };
};

const getSignOut = async () => {
  try {
    const res = await fetch(`/signout`);
    return res;
  } catch (err) {
    console.warn(err);
  };
};

const signIn = async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const signInData = {
    userId: formData.get('userId'),
    password: formData.get('password')
  };
  const { url } = await postSignIn(signInData);
  if (url && url !== '') {
    window.location.href = url
  };
};

const signOut = async (e) => {
  e.preventDefault();
  const { url } = await getSignOut();
  if (url && url !== '') {
    window.location.href = url
  };
};

document.addEventListener('DOMContentLoaded', async () => {
  // * index
  const signInForm = document.querySelector('#sign-in-form');
  signInForm?.addEventListener('submit', signIn);

  // * error
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.has('message')) {
    const message = urlParams.get('message')
    const msg = document.querySelector('.msg');
    msg.textContent = message;
  }

  // * member
  const signOutForm = document.querySelector('#sign-out-form');
  signOutForm?.addEventListener('submit', signOut);
});