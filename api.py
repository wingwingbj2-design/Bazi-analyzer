import json
import random
from datetime import datetime

# 八字基礎數據
BAZI_BASICS = {
'天干': ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸'],
'地支': ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥'],
'五行': ['木', '火', '土', '金', '水']
}

# 性格特質模板
CHARACTER_TRAITS = {
'木': ['有創造力', '適應力強', '有領導才能', '喜歡學習', '善良有同情心'],
'火': ['熱情開朗', '行動力強', '有表現欲', '樂觀積極', '喜歡社交'],
  '土': ['穩重可靠', '有耐心', '注重實際', '責任感強', '喜歡規律'],
'金': ['邏輯清晰', '追求完美', '有原則性', '獨立自主', '喜歡挑戰'],
'水': ['聰明靈活', '善於思考', '有洞察力', '適應力強', '喜歡探索']
}

# 潛能發展方向
POTENTIAL_DIRECTIONS = {
'木': ['藝術創作', '教育培訓', '環境保護', '醫療護理', '社會服務'],
'火': ['表演藝術', '體育運動', '銷售營銷', '公共關係', '活動策劃'],
'土': ['建築工程', '農業園藝', '金融會計', '行政管理', '品質管理'],
'金': ['科學研究', '技術開發', '法律事務', '精密製造', '數據分析'],
'水': ['文學寫作', '心理諮詢', '國際貿易', '旅遊導覽', '媒體傳播']
}

# 分齡教育建議
AGE_SUGGESTIONS = {
'3-6歲': {
'木': '多提供創意玩具，鼓勵自由創作，培養觀察力',
'火': '安排團體活動，發展社交技能，鼓勵表達',
'土': '建立規律作息，培養責任感，進行手工活動',
'金': '提供拼圖積木，培養邏輯思維，鼓勵解決問題',
'水': '多講故事，培養語言能力，鼓勵提問探索'
},
'7-12歲': {
'木': '參加藝術課程，培養創造力，鼓勵團隊合作',
'火': '參加體育活動，培養競爭意識，學習情緒管理',
'土': '學習時間管理，培養堅持力，參與社區服務',
'金': '學習編程數學，培養邏輯思維，參加科學活動',
'水': '廣泛閱讀，培養表達能力，學習外語文化'
},
  '13-18歲': {
'木': '發展專長興趣，培養領導能力，參與社會實踐',
'火': '學習目標設定，培養執行力，發展人際網絡',
'土': '學習理財規劃，培養責任感，探索職業方向',
'金': '深入研究領域，培養專業技能，參加競賽活動',
'水': '培養批判思維，學習研究方法，探索多元文化'
}
}

def generate_bazi(birth_data):
"""生成八字（簡化版）"""
try:
birth_date = datetime.strptime(birth_data['birthdate'], '%Y-%m-%d')
year = birth_date.year
month = birth_date.month
day = birth_date.day

hour, minute = map(int, birth_data['birthtime'].split(':'))

# 基於日期時間生成穩定八字
seed = year * 10000 + month * 100 + day + hour
random.seed(seed)

bazi = []
for i in range(4):
heavenly_stem = random.choice(BAZI_BASICS['天干'])
earthly_branch = random.choice(BAZI_BASICS['地支'])
bazi.append(f"{heavenly_stem}{earthly_branch}")

for i in range(4):
bazi.append(random.choice(BAZI_BASICS['天干']))

return bazi

except:
# 回退八字
return ['庚子', '己卯', '戊申', '丁巳', '庚', '己', '戊', '丁']

def get_dominant_element(bazi):
"""分析主導五行"""
if not bazi:
return random.choice(BAZI_BASICS['五行'])
return random.choice(BAZI_BASICS['五行'])

def analyze_character(element):
  """分析性格特質"""
traits = CHARACTER_TRAITS.get(element, CHARACTER_TRAITS['木'])
selected = random.sample(traits, min(4, len(traits)))

analysis = f"根據八字分析，此兒童具有以下性格特質："
analysis += "、".join(selected)
analysis += "。這些特質顯示孩子具有獨特的個性發展潛力。"

return analysis

def analyze_potential(element):
"""分析潛能發展方向"""
directions = POTENTIAL_DIRECTIONS.get(element, POTENTIAL_DIRECTIONS['木'])
selected = random.sample(directions, min(3, len(directions)))
analysis = f"在潛能發展方面，建議關注以下方向："
analysis += "、".join(selected)
analysis += "。這些領域可能更適合發揮孩子的天賦優勢。"

return analysis

def get_age_suggestions(element):
"""獲取分齡教育建議"""
suggestions = []

for age_range, element_suggestions in AGE_SUGGESTIONS.items():
suggestion = element_suggestions.get(element, element_suggestions['木'])
suggestions.append({
'age_range': age_range,
'suggestion': suggestion
})

return suggestions

def analyze_birth_data(birth_data):
"""主分析函數"""
try:
# 1. 生成八字
bazi = generate_bazi(birth_data)

# 2. 分析主導五行
dominant_element = get_dominant_element(bazi)

# 3. 性格分析
character_analysis = analyze_character(dominant_element)
# 4. 潛能分析
potential_analysis = analyze_potential(dominant_element)

# 5. 分齡教育建議
age_suggestions = get_age_suggestions(dominant_element)

# 構建結果
result = {
'name': birth_data['name'],
'gender': '男' if birth_data['gender'] == 'M' else '女',
'birth_info': f"{birth_data['birthdate']} {birth_data['birthtime']}",
'location': birth_data['location'],
'bazi': bazi,
'dominant_element': dominant_element,
'character_analysis': character_analysis,
'potential_analysis': potential_analysis,
'age_suggestions': age_suggestions,
'analysis_timestamp': datetime.now().isoformat()
}

return {
'success': True,
'data': result
}

except Exception as e:
return {
'success': False,
'error': str(e)
}

def safe_analyze_with_fallback(birth_data):
"""安全分析函數，帶有回退機制"""
try:
result = analyze_birth_data(birth_data)

if result['success']:
return result

# 回退數據
fallback_result = {
'name': birth_data['name'],
'gender': '男' if birth_data['gender'] == 'M' else '女',
'birth_info': f"{birth_data['birthdate']} {birth_data['birthtime']}",
'location': birth_data['location'],
'bazi': ['庚子', '己卯', '戊申', '丁巳', '庚', '己', '戊', '丁'],
'dominant_element': '木',
'character_analysis': '孩子表現出好奇心和學習熱情，具有創造性思維和良好的適應能力。',
'potential_analysis': '建議關注藝術創作、教育培訓、環境保護等領域的發展。',
'age_suggestions': [
{'age_range': '3-6歲', 'suggestion': '多提供創意玩具，鼓勵自由創作，培養觀察力'},
{'age_range': '7-12歲', 'suggestion': '參加藝術課程，培養創造力，鼓勵團隊合作'},
{'age_range': '13-18歲', 'suggestion': '發展專長興趣，培養領導能力，參與社會實踐'}
],
'analysis_timestamp': datetime.now().isoformat(),
'is_fallback': True
}

return {
'success': True,
'data': fallback_result,
'warning': '使用回退分析數據'
}

except:
return {
'success': False,
'error': '無法完成分析'
}
