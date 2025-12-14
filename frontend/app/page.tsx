const TopPage = async () => {
  const res = await fetch("http://127.0.0.1:8000")
  const data = res.json(); 
  console.log(data);
  return (
    <div>p</div>
  )
}

export default TopPage