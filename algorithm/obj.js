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


// 反向擦操作

const a = {
  a: 1,
  'b.c': 2,
  'b.d.e': 3,
  'b.d.f': 4,
  'g.0': 5,
  'g.1': 6,
  'g.2.h': 7
}

const nest = (obj) => {
  // console.log(obj)
  const rto = {}

  for (const key in obj) {
    const keyArr = key.split('.')
    let current = rto

    for (let i = 0; i < keyArr.length; ++i) {
      const cKey = keyArr[i]
      //  最后一个
      if (i === keyArr.length - 1) {
        current[cKey] = obj[key]
      } else {
        if (!current[cKey]) {
          // debugger
          // NaN 不等于 NaN
          if (+keyArr[i + 1] === +keyArr[i + 1]) {
            current[cKey] = []
          } else {
            current[cKey] = {}
          }
        }
        // 保存当前对象 继续向下面取值
        current = current[cKey]
      }
    }
  }
  return rto
}
nest(a)

