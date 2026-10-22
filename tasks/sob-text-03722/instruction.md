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
Rhodes Scholarship: The Rhodes Scholarship, named for the British mining magnate and South African politician Cecil John Rhodes, is an international postgraduate award for students to study at the University of Oxford.  It is widely considered to be one of the world's most prestigious scholarships. Established in 1902, it was the first large-scale programme of international scholarships, inspiring the creation of a great many other awards across the globe.

Rhodes Memorial: Rhodes Memorial on Devil's Peak in Cape Town, South Africa, is a memorial to English-born, South African politician Cecil John Rhodes (1853–1902).  The memorial was designed by the renowned architect, Sir Herbert Baker.

Cecil Rhodes: Cecil John Rhodes PC (5 July 1853 – 26 March 1902) was a British businessman, mining magnate and politician in South Africa, who served as Prime Minister of the Cape Colony from 1890 to 1896.  An ardent believer in British imperialism, Rhodes and his British South Africa Company founded the southern African territory of Rhodesia (now Zimbabwe and Zambia), which the company named after him in 1895.  South Africa's Rhodes University is also named after him.  Rhodes set up the provisions of the Rhodes Scholarship, which is funded by his estate, and put much effort towards his vision of a Cape to Cairo Railway through British territory.

Trader Horn: Alfred Aloysius "Trader" Horn (born Alfred Aloysius Smith; 1861–1931) was an ivory trader in central Africa.  He wrote a book, "Trader Horn: A Young Man's Astounding Adventures in 19th-Century Equatorial Africa" (ISBN  ), detailing his journeys into jungles teeming with buffalo, gorillas, man-eating leopards, serpents and "savages".  The book also documents his efforts to free slaves, meet the founder of Rhodesia, Cecil Rhodes, and liberate a princess from captivity.

Rhodes Estate Preparatory School: Rhodes Estate Preparatory School (known informally as REPS or R.E.P.S) is an all-boys' private boarding preparatory school in Matopos, Bulawayo, Zimbabwe near the Matobo National Park.  Founded in 1932, its completion was funded by the estate of Cecil John Rhodes, after whom it is named and whose summer home is located on the main site.  The school is modelled after the traditional British public school in terms of system, structure and traditions due to its deep English roots.

Rhodes Fruit Farms: Rhodes Fruit Farms, founded by Cecil John Rhodes in 1902, exists today as Boschendal The Estate, one of the oldest wine estates in South Africa.

South African College Schools: The South African College Schools is a primary and secondary education institution in Newlands, Cape Town, South Africa.  Founded in 1829, it is the oldest in South Africa.  SACS is one of four schools expressly named by Cecil John Rhodes to offer an annual Rhodes Scholarship to one of its graduating students.  The schools are a combination of the South African College Junior School and the South African College High School.

William Gaul: William Thomas Gaul (1850–1927) was Rector of All Saints Church, Du Toit's Pan, Kimberley, afterwards of St Cyprian's Church, Kimberley, Rural Dean of Griqualand West, and Archdeacon in what was still the Diocese of Bloemfontein, before being elected the second Bishop of Mashonaland, where he styled himself "the smallest bishop with the largest diocese in Christendom."  He officiated at the funeral of Cecil John Rhodes and helped draft the Rhodes Trust Deed.

Trader Horn (1931 film): Trader Horn is a 1931 American Pre-Code adventure film starring Harry Carey and Edwina Booth, and directed by W.S. Van Dyke.  It is the first non-documentary film shot on location in Africa.  The film is based on the book of the same name by trader and adventurer Alfred Aloysius Horn and tells of adventures on safari in Africa.

James Rose Innes: Sir James Rose Innes, {'1': ", '2': ", '3': ", '4': "} PC (8 January 1855 – 16 January 1942) was the Chief Justice of South Africa from 1914 to 1927 and, in the view of many, its greatest ever judge.  Before becoming a judge he was a member of the Cape Parliament, the Cape Colony's Attorney-General, and a prominent critic of Cecil John Rhodes.

Question: Who was born first Alfred Aloysius "Trader" Horn or Cecil John Rhodes PC

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_born_first": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person born first."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the person born first."
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "person_born_second": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person born second."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the person born second."
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "comparison_result": {
      "type": "string",
      "description": "A statement indicating who was born first."
    }
  },
  "required": [
    "person_born_first",
    "person_born_second",
    "comparison_result"
  ],
  "additionalProperties": false
}
