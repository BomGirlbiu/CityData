import { mergeRecursive } from "@/utils/ruoyi";
import dictConverter from './DictConverter'
// 这段代码定义了一个模块，它提供了字典数据的请求、转换和合并选项的功能。以下是代码的主要组成部分和它们的功能：

export const options = {
  // /一个对象，包含所有字典类型的元数据。在这个例子中，'*' 表示默认的字典元数据，它将被应用到所有字典类型，除非为特定类型提供了更具体的元数据。
  metas: {
    '*': {
      /**
       * 字典请求，方法签名为function(dictMeta: DictMeta): Promise
       */
      request: (dictMeta) => {
        console.log(`load dict ${dictMeta.type}`)
        return Promise.resolve([])
      },
      /**
       * 字典响应数据转换器，方法签名为function(response: Object, dictMeta: DictMeta): DictData
       */
      responseConverter,
      labelField: 'label',
      valueField: 'value',
    },
  },
  /**
   * 默认标签字段
   */
  DEFAULT_LABEL_FIELDS: ['label', 'name', 'title'],
  /**
   * 默认值字段
   */
  DEFAULT_VALUE_FIELDS: ['value', 'id', 'uid', 'key'],
}

/**
 * 映射字典
 * @param {Object} response 字典数据
 * @param {DictMeta} dictMeta 字典元数据
 * @returns {DictData}
 */
function responseConverter(response, dictMeta) {
  const dicts = response.content instanceof Array ? response.content : response
  if (dicts === undefined) {
    console.warn(`no dict data of "${dictMeta.type}" found in the response`)
    return []
  }
  return dicts.map(d => dictConverter(d, dictMeta))
}

export function mergeOptions(src) {
  mergeRecursive(options, src)
}

export default options
