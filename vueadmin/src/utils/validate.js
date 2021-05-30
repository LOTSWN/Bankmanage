/**
 * Created by PanJiaChen on 16/11/18.
 */

/**
 * @param {string} path
 * @returns {Boolean}
 */
export function isExternal(path) {
  return /^(https?:|mailto:|tel:)/.test(path)
}

/**
 * @param {string} str
 * @returns {Boolean}
 */
export function validUsername(str) {
  const valid_map = ['admin', 'editor']
  $.post("/login",str.trim(),function(backstr){
          if(backstr=="find") return 1;
          else return 0;
  });
  // return valid_map.indexOf(str.trim()) >= 0
}
