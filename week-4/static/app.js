const postSignIn = async ({ username, password }) => {
  try {
    const res = await fetch(`${window.location.host}/signin`, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({username, password})
    });
    return res;
  } catch (err) {
    console.warn(err);
  };
};

const signIn = async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const signInData = {
    username: formData.get('username'),
    password: formData.get('password')
  };
  const { msg } = await postSignIn(signInData);
  console.log(msg);
}

document.addEventListener('DOMContentLoaded', async () => {
  console.log('YOOOOOOOO', window.location.host);
  const signInForm = document.querySelector('#sign-in-form');
  signInForm.addEventListener('submit', signIn);

});