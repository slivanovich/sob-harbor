Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Islam in Hong Kong: Islam is practised in :Hong Kong by about 300,000 Muslims.  About 12,000 of the Muslim families in Hong Kong are 'local boy' families, Muslims of mixed Chinese and South Asian ancestry descended from early Muslim South Asian immigrants who took local Chinese wives (( Tanka )) and brought their children up as Muslims.  Hui Muslims from Mainland China also played a role in the development of Islam in Hong Kong, such as Kasim Tuet from Guangzhou, one of the pioneers of Muslim education in the city, for who the Islamic Kasim Tuet Memorial College is named.  In the new millennium, the largest number of Muslims in the territory are Indonesian, in which most of them are female foreign domestic workers.  They account for over 120,000 of Hong Kong's Muslim population.  The vast majority of Muslims in Hong Kong are Sunni.

New towns of Hong Kong: New Towns in Hong Kong are areas that the Hong Kong government started developing in the 1950s, in order to accommodate the booming population.  At the first phase of development, the newly developed towns were called "satellite town", a concept borrowed from the United Kingdom, of which Hong Kong was then still a colony.  Kwun Tong, located at eastern Kowloon, and Tsuen Wan, located at the south-west New Territories, were designated as the first two satellite towns, when the urban area in Hong Kong was still relatively small, restricted to the central and western part of Kowloon Peninsula and the northern side of Hong Kong Island.  Wah Fu Estate was also built in a remote corner at the southern side of Hong Kong Island, with similar concepts in a smaller scale.

Industrial and Commercial Bank of China (Canada): Industrial and Commercial Bank of China (Canada), formerly The Bank of East Asia (Canada), was founded in 1991; it was the Canadian unit of the Bank of East Asia Group (BEA) in Hong Kong.  The bank operates five branches in Canada and offers retail banking products catering to expatriate Hong Kong Chinese in Canada.  The bank operated at Hong Kong Chinese themed malls or areas with large Hong Kong Chinese population.  A 70% stake of the bank was sold by former parent Bank of East Asia in January 2010 to Industrial and Commercial Bank of China and on July 2 the bank changed its name to the current name.  BEA retains a 30% stake as BEA focuses business in Hong Kong.  Signage at all Canadian branches were changed to reflect the new ownership.  BEA Canada is the second Hong Kong based bank to pull its Canadian operations.  Standard Chartered Bank (Hong Kong) sold its Canadian branches and operations to Bank of Montreal and Scotiabank respectively in the 1990s.

Sha Tin District: Sha Tin District () is one of the 18 districts of Hong Kong.  As one of the 9 districts located in the New Territories, it covers the areas of Sha Tin, Tai Wai, Ma On Shan, Fo Tan, Siu Lek Yuen and Ma Liu Shui.  The district is the most populous district in Hong Kong, with a population of 630,273, having a larger population than many countries or dependencies including Iceland, Macau, Montenegro and Brunei.

Taishanese people in Hong Kong: Sze Yap Cantonese (Chinese: 四邑廣東人; Taishanese: Sli Yip Gong Ong Ngin; Cantonese: Sei Yap Gwong Dong Yan; Mandarin: Si Yi Guang Dong Ren) represents the second largest Han group in Hong Kong after the group of people originating from the Guangzhou-Sam Yap region.  The Sze Yap Cantonese comes from a region in Guangdong in China called Sze Yap (四邑), now called Ng Yap, which consists of the cities of Taishan, Kaiping, Xinhui, Enping, Heshan and Jiangmen.  The Sze Yap Cantonese group have contributed much to what makes Hong Kong a success.  In the 1960s, Hong Kong people of Sze Yap origin represented about 30% of Hong Kong's total population and today this population still increases as more immigrants from the Taishanese speaking areas of Guangdong in mainland China continue to immigrate to Hong Kong.

Wuzhong, Ningxia: Wuzhong () is a prefecture-level city in the Ningxia autonomous region of the People's Republic of China.  It was known as Yinnan Prefecture () before it was upgraded to a prefecture-level city in 1998.  In 2010, Wuzhong had a population of 1.3 million.

Hong Kong: Hong Kong, officially the Hong Kong Special Administrative Region of the People's Republic of China, is an autonomous territory south to Mainland China and east to Macao in East Asia.  With around 7.2 million Hong Kongers of various nationalities in a territory of 1,104 km, Hong Kong is the world's fourth most densely populated country or territory.

Nepalis in Hong Kong: There is a moderate ethnic minority population of Nepalese people in Hong Kong (referred to as 'Hong Kong Nepalese'), forming roughly 0.5% of the total population (approximately 40,000 Hong Kong Nepalese citizens).  They primarily came to the territory as part of the Gurkha brigade of the British Army.  After the handover in 1997, they were permitted to stay in Hong Kong.  Majority of the Nepali population of Hong Kong are the children and grandchildren of Gurkha soldiers who were fierce fighters serving the British Army from 1814.

Youth in Hong Kong: Youth in Hong Kong, according to the University of Hong Kong Statistical Profile, includes citizens of the Chinese territory of Hong Kong aged 15–24 years.  As of 2011, youth in Hong Kong ages 15–24 made up 12.4% of Hong Kong's overall population at 875,200 people.  Hong Kong is a hybrid culture, influenced by China and Britain, but overall by its international economic ties, which plays a role in shaping the lives of the youth in Hong Kong.  The youth in Hong Kong are unique in the fact that many are living Transnationalist identities.  The demographics are not just ethnically Chinese youth in Hong Kong, but also youth that are ethnically White, Indonesian, Filipino, which can be seen in Demographics of Hong Kong, and that creates a unique society.  "Although with a dominant Chinese population, Hong Kong is an international city and is a mix of East and West rich in cultures, history, and religions."  The disparity between the rich and poor within Hong Kong has been growing wider.

New Territories: New Territories () is one of the three main regions of Hong Kong, alongside Hong Kong Island and the Kowloon Peninsula.  It makes up 86.2% of Hong Kong's territory, and contains around half of the population of Hong Kong.  Historically, it is the region described in The Convention for the Extension of Hong Kong Territory.  According to that the territories comprise the mainland area north of the Boundary Street of Kowloon Peninsula and south of the Sham Chun River which is the border between Hong Kong and Mainland China, as well as over 200 outlying Islands including Lantau Island, Lamma Island, Cheung Chau, and Peng Chau in the territory of Hong Kong.

Question: Does Hong Kong or Wuzhong, Ningxia have a larger population?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_a_name": {
      "type": "string",
      "description": "The name of the first entity being compared."
    },
    "entity_a_population": {
      "type": "number",
      "description": "The population of the first entity."
    },
    "entity_b_name": {
      "type": "string",
      "description": "The name of the second entity being compared."
    },
    "entity_b_population": {
      "type": "number",
      "description": "The population of the second entity."
    },
    "larger_population_entity": {
      "type": "string",
      "description": "The name of the entity with the larger population."
    },
    "population_difference": {
      "type": "number",
      "description": "The difference in population between the two entities."
    }
  },
  "required": [
    "entity_a_name",
    "entity_a_population",
    "entity_b_name",
    "entity_b_population",
    "larger_population_entity",
    "population_difference"
  ],
  "additionalProperties": false
}
