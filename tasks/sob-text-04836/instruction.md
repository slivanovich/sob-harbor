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
Battle of Karnal: The Battle of Karnal (February 24, 1739), was a decisive victory for Nader Shah of Iran, during his invasion of Mughal dynasty of India.  Nader's forces defeated the army of Muhammad Shah within three hours, despite being heavily outnumbered (six-to-one), paving the way for the Persian sack of Delhi.  The engagement is considered the crowning jewel in Nader's military career as well as a tactical masterpiece.  The battle took place near Karnal, 110 km north of Delhi, India.

Munger Fort: The Munger Fort, located at Munger (also spelt as Monghyr during the British Raj), in the state of Bihar, India, is built on a rocky hillock on the south bank of the Ganges River.  Its history is not completely dated but it is believed that it was built during the early rule of Slave dynasty of India.  The Munger town where the fort is situated was under the control of Muhammad bin Tughluq of Delhi (1325-1351 AD).  The fort has two prominent hills called the Karnachaura or Karanchaura, and the other a built up rectangular mound deduced to be the location of a citadel of the fort with historical links.  The Fort had a succession of Muslim rulers (Khaljis, Tughlaqs, Lodis, Nawabs of Bengal, followed by Mughal rulers, till it was finally acceded to the British by Mir Quasim (1760–72), after unseating his father-in-aw Mīr Jafar on the grounds of old age, for a monetary reward negotiated by Vansittart.  This deal involved payment by the East India Company’s merchants of an ad valorem duty of 9 percent, against an Indian merchant’s duty of 40%.  The fort became a place of considerable importance to the British in Bengal till 1947 (India'a independence).

Gujarat under Mughal Empire: In 1573, Akbar (1573-1605), the emperor of the Mughal Empire captured Gujarat (now a state in western India) by defeating Gujarat Sultanate under Muzaffar Shah III.  Muzaffar tried to regain the Sultanate in 1584 but failed.  Gujarat remained the Mughal province ("subah") governed by the viceroys and officers appointed by the Mughal emperors from Delhi.  Akbar's foster brother Mirza Aziz Kokaltash was appointed as the viceroy who strenghthened Mughal hold over the region.  The nobles of former Sultanate continued to resist and rebel during the reign of the next emperor Jehangir (1605-1627) but Kokaltash and his successor viceroys subdued them.  Jehangir also permitted the British East India Company to establish factories in Surat and elsewhere in Gujarat.  The next emperor Shah Jahan (1627-1658) expanded his terrotories in south and his viceroys made hold over Kathiawar peninsula including Nawanagar.  Shah Jahan had also appointed his prince Aurangzeb, who was involved in religious disputes, prince Dara Shikoh and later prince Murad Bakhsh as viceroys.  Following battle of succession, Aurangzeb (1658-1707) came to the Mughal throne and his policies resulted in revolts and discontent.  During his reign, the Marathas under Shivaji raided Surat (1666) and their incursions in Gujarat started.  Till then Gujarat prospered due to political stability, peace and growing international trade.

Agra Fort: Agra Fort is a historical fort in the city of Agra in India.  It was the main residence of the emperors of the Mughal Dynasty till 1638, when the capital was shifted from Agra to Delhi.  The Agra fort is a UNESCO World Heritage site.  It is about 2.5 km northwest of its more famous sister monument, the Taj Mahal.  The fort can be more accurately described as a walled city.

Red Fort: The Red Fort is a historical fort in the city of Delhi in India.  It was the main residence of the emperors of the Mughal dynasty for nearly 200 years, until 1857.  It is located in the center of Delhi and houses a number of museums.  In addition to accommodating the emperors and their households, it was the ceremonial and political centre of the Mughal state and the setting for events critically impacting the region.

Peacock Throne: The Peacock Throne (Hindustani: मयूर ارباب حلقه ها, تخت طاؤس : "Mayūr Singhāsana", Persian: تخت طاووس‎ ‎ , "Takht-i Tāvūs") was a famous jeweled throne that was the seat of the Mughal emperors of India.  It was commissioned in the early 17th century by emperor Shah Jahan and was located in the Diwan-i-Khas (Hall of Private Audiences) in the Red Fort of Delhi.  The original throne was subsequently captured and taken as a war trophy in 1739 by the Persian king Nadir Shah, and has been lost ever since.  A replacement throne based on the original was commissioned afterwards and existed until the Indian war of Independence in 1857.

Salimgarh Fort: Salimgarh Fort (Hindi: सलीमगढ़ किला , Urdu: ‎ ،literally "Salim’s Fort") was built in 1546 AD, in Delhi, in a former island of the Yamuna River, by Salim Shah Suri, son of Sher Shah Suri.  There was a pause in Mughal rule when in 1540 AD Sher Shah Suri defeated the Mughal Emperor Humayun (and ousted him from Delhi) and established the Sur dynasty rule in Delhi.  Sur dynasty rule lasted till 1555 AD when Humayun regained his kingdom by defeating Sikander Suri, the last ruler of the dynasty.  During the Mughal period, in later years, while building the Red Fort and Shahjahanbad, several Mughal rulers including Emperor Shahjahan who is credited with completing Shahjahanabad in 1639 AD had camped at this fort.  It is said that Humayun had camped at this fort for three days before launching his successful attack for recapturing Delhi.

Akbar Shah (diamond): The Akbar Shāh, also known as the "Lustre of the Peacock Throne", is a diamond dating back to the Mughal dynasty of India.  It is an irregular, pear-shaped diamond with a light green hue, weighing 73.60 carat.

Gur-e-Amir: The Gūr-i Amīr or Guri Amir (Uzbek: "Amir Temur maqbarasi, Go'ri Amir" , Persian: ‎ ‎ ), is a mausoleum of the Asian conqueror Timur (also known as Tamerlane) in Samarkand, Uzbekistan.  It occupies an important place in the history of Persian-Mongolian Architecture as the precursor and model for later great Mughal architecture tombs, including Gardens of Babur in Kabul, Humayun's Tomb in Delhi and the Taj Mahal in Agra, built by Timur's Persianised descendants, the ruling Mughal dynasty of North India.  It has been heavily restored.

Mughal emperors: The Mughal emperors, from the early 16th century to the early 18th century, built and ruled the Mughal Empire on the Indian subcontinent, mainly corresponding to the modern countries of Bangladesh, India and Pakistan.  The Mughals were a branch of the Timurid dynasty.  Their power rapidly dwindled during the 18th century and the last of the emperors was deposed in 1857, with the establishment of the British Raj.  The dynasty had Turco-Mongol roots from a Central Asian area now part of modern-day Uzbekistan, and the emperors claimed direct descent from both Timur (generally known in the West as Tamerlane the Great) and Genghis Khan, through his son Chagatai Khan.

Question:  Peacock Throne was located in what historical fort in the city of Delhi in India that was the main residence of the emperors of the Mughal dynasty

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "fort_name": {
      "type": "string",
      "description": "The name of the historical fort."
    },
    "city": {
      "type": "string",
      "description": "The city where the fort is located."
    },
    "country": {
      "type": "string",
      "description": "The country where the fort is located."
    },
    "historical_significance": {
      "type": "string",
      "description": "A description of the fort's historical importance, particularly its role as a residence for Mughal emperors."
    },
    "throne_specific_location": {
      "type": "string",
      "description": "The specific location within the fort where the Peacock Throne was situated."
    }
  },
  "required": [
    "fort_name",
    "city",
    "country",
    "historical_significance",
    "throne_specific_location"
  ],
  "additionalProperties": false
}
