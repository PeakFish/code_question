const thounght = (num) => {
  const arrNum = String(num).split('').reverse()
  // const len = arrNum.length
  // const befLen = len % 3
  const result = arrNum.reduce((pv, cv, ci) => {
    const aci = ci + 1
    if (aci % 3 === 0 && aci !== arrNum.length) {
      return '' + pv + cv + ','
    } else {
      return '' + pv + cv
    }
  })
  return result.split('').reverse().join('')
}
thounght(123456789)
