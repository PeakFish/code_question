// 对象转化成平坦的对象
const obj = { a: 1, b: { c: 2, d: { e: 3, f: 4 }}, g: [5, 6, { h: 7 }]};
const flatObj = {};

function flat(keys, obj) {
  for (let key in obj) {
    if (obj[key] && typeof obj[key] === "object")  {
      flat(keys.concat(key), obj[key]);
    } else {
      flatObj[keys.concat(key).join('.')] = obj[key];
    }
  }
}
flat([], obj);


// 反向擦操作（未完成）

const a = {
  "a": 1, "b.c": 2,
  "b.d.e": 3, "b.d.f": 4,
  "g.0": 5, "g.1": 6, "g.2.h": 7
}

const nest = (obj) => {
  console.log(obj);
  const rto = {}

  for (var key in obj) {
  	var keyArr = key.split('.');
    let current = rto;

    for (var i = 0; i < keyArr.length; ++i) {
      if(i === key.length - 1) {
        current[key] = obj[key]
      } else {
        if (!current[key]) {
          if(+keyArr[i + 1] === +keyArr[i + 1]) {
            current[key]=[]
          }
        } else {
          current[key] = {}
        }
        current = current[key];
      }
    }

  }
}
