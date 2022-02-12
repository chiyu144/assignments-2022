// * 發 API 用
const postSignUp = async({ userName, userId, password }) => {
  try {
    const res = await fetch(`/signup`, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({userName, userId, password})
    });
    return res;
  } catch (err) {
    console.warn(err);
  }
};
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

// * 事件處理
const signUp = async (e) => {
  e.preventDefault();
  console.log('Test');
  const formData = new FormData(e.target);
  const signUpData = {
    userName: formData.get('new-user-name'),
    userId: formData.get('new-user-id'),
    password: formData.get('new-user-password')
  };
  const { url } = await postSignUp(signUpData);
  if (url && url !== '') {
    window.location.href = url
  };
};

const signIn = async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const signInData = {
    userId: formData.get('user-id'),
    password: formData.get('user-password')
  };
  const { url } = await postSignIn(signInData);
  if (url && url !== '') {
    window.location.href = url
  };
};

document.addEventListener('DOMContentLoaded', async () => {
  const signUpForm = document.querySelector('#sign-up-form');
  signUpForm?.addEventListener('submit', signUp);

  const signInForm = document.querySelector('#sign-in-form');
  signInForm?.addEventListener('submit', signIn);
});