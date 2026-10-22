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
Teeny Ted from Turnip Town: Teeny Ted from Turnip Town (2007), published by Robert Chaplin, is certified by "Guinness World Records" as the world's smallest reproduction of a printed book.  The book was produced in the Nano Imaging Laboratory at Simon Fraser University in Vancouver, British Columbia, Canada, with the assistance of SFU scientists Li Yang and Karen Kavanagh.

Hsu Li Yang: Hsu Li Yang (born 1972) is a Singapore chess International Master.  He won the national Singaporean Chess Championship in 1992 and 1993.  Represented Singapore three times in Chess Olympiads (1992, 1994, 2000).  His current FIDE rating is 2427.

Li Yang (director): Li Yang (; born 1959) is a Chinese writer-director.  Though often grouped with the so-called Sixth Generation of Chinese filmmakers, he is in fact closer in age to the Fifth Generation and in interviews has denied membership with either group, claiming that such labels are only artificial differentiations.

Li Yang (ski jumper): Li Yang (; born 31 March 1980 in Tonghua, Jilin) is a Chinese ski jumper who has been competing since 2004.  At the 2006 Winter Olympics, he finished 16th in the team large hill and 44th in the individual normal hill events.

Emperor Gong of Sui: Emperor Gong of Sui (隋恭帝) (605 – 14 September 619), personal name Yang You (楊侑), was an emperor of the Chinese Sui Dynasty.  Traditionally, he was considered the last emperor of the dynasty because he was the one who formally yielded the throne to the founding emperor to the succeeding Tang Dynasty, Emperor Gaozu of Tang (Li Yuan), although after him, his brother Yang Tong claimed the throne and continued to do so until 619.  Li had rebelled against the rule of Yang You's grandfather Emperor Yang of Sui in 617 and captured the capital Chang'an later that year, seizing Yang You and declaring him emperor, although only the commanderies under Li's control recognized him as emperor; the rest of the commanderies continued to recognize Emperor Yang as emperor.  In 618, after news arrived that Emperor Yang had been killed by the general Yuwen Huaji, Li had the young emperor yield the throne to him.  The former emperor died the following year, probably on the new emperor's orders.

Li Mi (Sui dynasty): Li Mi (李密) (582–619), courtesy name Xuansui (玄邃), pseudonym Liu Zhiyuan (劉智遠), was the leader of a rebel movement against the rule of the Chinese Sui dynasty.  He initially was the strategist of the Sui general Yang Xuangan, who rebelled against Emperor Yang of Sui in 613 but failed, and Li subsequently led a rebellion against Emperor Yang in his own right in 617.  He gained so much following that there was widespread expectation that he soon would be able to prevail over Sui forces and establish a new dynasty—so much so that even other key rebel leaders, including Dou Jiande, Meng Haigong (孟海公), Xu Yuanlang, and Zhu Can, were urging him to take imperial title.  Even Li Yuan (soon to become the founder of the Tang dynasty as Emperor Gaozu was writing him in supplicating terms that implicitly supported his imperial claim.  Li Mi tried to gain control of the Sui eastern capital Luoyang, but his forced became stalemated by the Sui forces there, and he never came around to claiming the imperial title, instead accepting the title of Duke of Wei.  In October 618, the Sui general Wang Shichong crushed his forces at Yanshi.  Li Mi fled to Tang territory and submitted to Emperor Gaozu, but subsequently rebelled against Tang and tried to revive his own army.  The Tang general Sheng Yanshi (盛彥師) captured and executed him.

Li Yixiang: Li Yixiang (), also known as Li Qiang (李强), is a Chinese actor.  He appeared in movies such as "Ji Quan Bu Ning", "Crazy Lottery".  In 2002, he starred as one of the two murderous con men in director Li Yang's "Blind Shaft", opposite Wang Baoqiang as his naive would-be victim.  Li shared the Golden Kinnaree for Best Actor at the 2004 Bangkok International Film Festival along with Wang, and fellow "Blind Shaft" co-star, Wang Shuangbao.

Bill Duke: William Henry "Bill" Duke, Jr. (born February 26, 1943) is an American actor and film director.  Known for his physically imposing frame, Duke's work frequently dwells within the action and crime drama genres but also appears in comedy.  He often plays characters related to law enforcement.

Yuwen Shu: Yuwen Shu (宇文述) (died 616), courtesy name Botong (伯通), formally Duke Gong of Xu (許恭公), was an official and general of the Chinese dynasty Sui Dynasty.  He was a confidant of Emperor Yang (Yang Guang) and was instrumental in Yang Guang's displacement of his brother Yang Yong as crown prince; therefore, after Yang Guang became emperor, Yuwen Shu became exceedingly powerful and was one of two generals who spearheaded Yangdi's efforts in the Goguryeo-Sui Wars.  His son Yuwen Huaji later led a coup against Emperor Yang in 618 and, after killing Emperor Yang, briefly claimed imperial title in 619, but was soon captured and killed.  Another son of Yuwen Shu, Yuwen Shiji, however, was a friend of Tang Dynasty's founder Li Yuan (Emperor Gaozu), and after Li Yuan established Tang remained an influential official.

Blind Mountain: Blind Mountain () is a 2007 Chinese film directed by Li Yang and is Li's first feature film since his 2003 debut "Blind Shaft".  It is also known as "Road Home".

Question: what does Bill Duke and Li Yang have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1_name": {
      "type": "string",
      "description": "The name of the first person."
    },
    "person_2_name": {
      "type": "string",
      "description": "The name of the second person."
    },
    "shared_profession": {
      "type": "string",
      "description": "The profession or role that both individuals have in common."
    },
    "person_1_professions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of professions or roles for the first person."
    },
    "person_2_professions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of professions or roles for the second person."
    },
    "person_2_directed_films": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of films directed by the second person."
    }
  },
  "required": [
    "person_1_name",
    "person_2_name",
    "shared_profession",
    "person_1_professions",
    "person_2_professions",
    "person_2_directed_films"
  ],
  "additionalProperties": false
}
