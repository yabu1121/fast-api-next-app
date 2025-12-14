
export default Todo = async () => {
  const res = await fetch("http://127.0.0.1");
  const data = await res.json();
  console.log(res);
  console.log(data);
}