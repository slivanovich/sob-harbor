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
Seven Military Classics: The Seven Military Classics () were seven important military texts of ancient China, which also included Sun-tzu's "The Art of War".  The texts were canonized under this name during the 11th century AD, and from the time of the Song Dynasty, were included in most military encyclopedias. For imperial officers, either some or all of the works were required reading to merit promotion, like the requirement for all bureaucrats to learn and know the work of Confucius.

Six Secret Teachings: The Six Secret Teachings (), is a treatise on civil and military strategy traditionally attributed to Lü Shang (aka Jiang Ziya), a top general of King Wen of Zhou, founder of the Zhou dynasty, at around the eleventh century BC.  Modern historians nominally date its final composition to the Warring States period (c.475-221 BC), but some scholars believe that it preserves at least vestiges of ancient Qi political and military thought.  Because it is written from the perspective of a statesman attempting to overthrow the ruling Shang dynasty, it is the only one of the Seven Military Classics explicitly written from a revolutionary perspective.

Wuzi: The Wuzi () is a classic Chinese work on military strategy attributed to Wu Qi.  It is considered one of China's Seven Military Classics.

ILOVEYOU: ILOVEYOU, sometimes referred to as Love Bug or Love Letter, was a computer worm that attacked tens of millions of Windows personal computers on and after 5 May 2000 local time in the Philippines when it started spreading as an email message with the subject line "ILOVEYOU" and the attachment "LOVE-LETTER-FOR-YOU.txt. vbs".  The latter file extension ('vbs', a type of interpreted file) was most often hidden by default on Windows computers of the time (as it is an extensions for a file type that is known by Windows), leading unwitting users to think it was a normal text file.  Opening the attachment activated the Visual Basic script.  The worm did damage on the local machine, overwriting random types of files (including Office files, image files, and audio files; however after overwriting MP3 files the virus would hide the file), and sent a copy of itself to all addresses in the Windows Address Book used by Microsoft Outlook.  In contrast, the Melissa virus only sent copies to the first 500 contacts.  This made it spread much faster than any other previous email worm.

Wujing Zongyao: The Wujing Zongyao, sometimes rendered in English as the Complete Essentials for the Military Classics, is a Chinese military compendium written from around 1040 to 1044.  It contains the earliest known written chemical formulas for gunpowder, made from saltpeter, sulphur, and charcoal, along with many added ingredients.

The Art of War: The Art of War is an ancient Chinese military treatise dating from the Spring and Autumn period in 5th century BC.  The work, which is attributed to the ancient Chinese military strategist Sun Tzu ("Master Sun", also spelled Sunzi), is composed of 13 chapters.  Each one is devoted to a distinct aspect of warfare and how that applies to military strategy and tactics.  For almost 1,500 years it was the lead text in an anthology that would be formalised as the Seven Military Classics by Emperor Shenzong of Song in 1080.  "The Art of War" remains the most influential strategy text in East Asia.  It has also had an influence on Eastern and Western military thinking, business tactics, legal strategy and beyond.

Three Strategies of Huang Shigong: The Three Strategies of Huang Shigong () is a text on military strategy that was historically associated with the Han dynasty general Zhang Liang.  The text's literal name is ""the Three Strategies of the Duke of Yellow Rock"", based on the traditional account of the book's transmission to Zhang.  Modern scholars note the similarity between its philosophy and the philosophy of Huang-Lao Daoism.  It is one of China's Seven Military Classics.

Wei Liaozi: The Wei Liaozi () is a text on military strategy, one of the Seven Military Classics of ancient China.  It was written during the Warring States period.

Sun Tzu: Sun Tzu ( ; also rendered as Sun Zi 孫子) was a Chinese general, military strategist, and philosopher who lived in the Spring and Autumn period of ancient China.  Sun Tzu is traditionally credited as the author of "The Art of War", a widely influential work of military strategy that has affected both Western and Eastern philosophy.  Aside from his legacy as the author of "The Art of War", Sun Tzu is revered in Chinese and the Culture of Asia as a legendary historical figure.  His birth name was Sun Wu, and he was known outside of his family by his courtesy name Changqing.  The name "Sun Tzu" by which he is best known in the West is an honorific which means "Master Sun".

The Methods of the Sima: The Methods of the Sima (, also known as The Marshal's Art of War) is a text discussing laws, regulations, government policies, military organization, military administration, discipline, basic values, tactics, and strategy.  It is considered to be one of the Seven Military Classics of ancient China.  It was developed in the state of Qi during the 4th century BC, in the mid-Warring States period.

Question: Who wrote the book used as the lead text formalised as the Seven Military Classics?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "author": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the author."
        },
        "title": {
          "type": "string",
          "description": "The honorific title of the author."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Key roles or professions of the author."
        }
      },
      "required": [
        "name",
        "title",
        "roles"
      ],
      "additionalProperties": false
    },
    "book": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the book."
        },
        "status_in_classics": {
          "type": "string",
          "description": "The book's specific status or role within the Seven Military Classics."
        },
        "formalization_year": {
          "type": "integer",
          "description": "The year the Seven Military Classics were formalized."
        }
      },
      "required": [
        "title",
        "status_in_classics",
        "formalization_year"
      ],
      "additionalProperties": false
    },
    "collection_name": {
      "type": "string",
      "description": "The name of the collection the book belongs to."
    }
  },
  "required": [
    "author",
    "book",
    "collection_name"
  ],
  "additionalProperties": false
}
