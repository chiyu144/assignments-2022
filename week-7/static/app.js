// * 發 API 用
const postSignUp = async({ userName, userId, password }) => {
  try {
    const res = await fetch(`/signup`, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ userName, userId, password })
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
      body: JSON.stringify({ userId, password })
    });
    return res;
  } catch (err) {
    console.warn(err);
  };
};
const postUpdateMember = async ({ userName }) => {
  try {
    const res = await fetch(`/api/member`, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ userName })
    });
    return res;
  } catch (err) {
    console.warn(err);
  };
};
const getSearchMembers = async (searchUserId) => {
  try {
    const res = await fetch(`/api/members?username=${searchUserId}`, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }
    });
    return res;
  } catch (err) {
    console.warn(err);
  };
};
// * 事件處理
const signUp = async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const signUpData = {
    userName: formData.get('new-user-name'),
    userId: formData.get('new-user-id'),
    password: formData.get('new-user-password')
  };
  const { url, redirected } = await postSignUp(signUpData);
  if (redirected) {
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
  const { url, redirected } = await postSignIn(signInData);
  if (redirected) {
    window.location.href = url
  };
};
const updateMember = async(e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const updateData = {
    userName: !formData.get('update-name') ? null : formData.get('update-name')
  };
  const res = await postUpdateMember(updateData);
  const data = await res.json();

  const p = document.querySelector('#update-name-result');
  const headerTitle = document.querySelector('h2');
  if (data.ok) {
    p.textContent = '更新成功';
    headerTitle.textContent = `${updateData.userName}您好，這是會員頁`
  };
  if (data.error) { p.textContent = '更新失敗' };
};
const searchMembers = async(e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const searchUserId = !formData.get('search-user-id') ? undefined : formData.get('search-user-id');
  const res = await getSearchMembers(searchUserId);
  const { data } = await res.json()

  const p = document.querySelector('#search-members-result')
  p.textContent = !data ? '查無此人' : `${data.name}`
};
// * 監聽
document.addEventListener('DOMContentLoaded', async () => {
  const signUpForm = document.querySelector('#sign-up-form');
  signUpForm?.addEventListener('submit', signUp);

  const signInForm = document.querySelector('#sign-in-form');
  signInForm?.addEventListener('submit', signIn);

  const searchMembersForm = document.querySelector('#search-members-form');
  searchMembersForm?.addEventListener('submit', searchMembers);

  const updateMemberForm = document.querySelector('#update-member-form');
  updateMemberForm?.addEventListener('submit', updateMember);
});
