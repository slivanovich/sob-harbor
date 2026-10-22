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
Socolar: Socolar is a free searchable database of open access journals, and repositories hosted by the "China Educational Publications Import and Export Corporation" (CEPIEC), one of the largest state-owned companies that was established in 1987 to meet the demands of foreign academic publications from universities and colleges in China.  It links to more than 11,739 journals and more than 1048 repositories with about 23,795,416 articles in total in many languages.

Technology Transfer Center of Zhejiang University: The Technology Transfer Center of Zhejiang University (Simplified Chinese: 浙江大学技术转移中心), currently is the largest university technology transfer center in the People's Republic of China.  It's the main technology transfer department of the Zhejiang University in Hangzhou, Zhejiang Province.

C9 League: The C9 League is an official alliance of nine elite and prestigious universities in mainland China, initiated by the Chinese Central Government through Project 985 to promote the development and reputation of Chinese higher education system by founding world-class universities in the 21st century.  It is analogous to the Ivy League in the United States, the U15 in Canada, the Golden Triangle in the UK, and the Go8 in Australia.  The members of the C9 League are Tsinghua University, Peking University, Zhejiang University, Nanjing University, Fudan University, Shanghai Jiao Tong University, Xi'an Jiaotong University, University of Science and Technology of China and Harbin Institute of Technology.  Together they account for 3% of the country's researchers but receive 10% of national research expenditures.  They produce 20% of the nation's academic publications and 30% of total citations.

Zhejiang University of Technology: The Zhejiang University of Technology () is in the city of Hangzhou, Zhejiang Province.  It is considered one of the top industrial universities in mainland China and the second largest university in Zhejiang Province after the most comprehensive Zhejiang University.

Zhejiang University: Zhejiang University (ZJU, also known as Che Kiang University; ), sometimes referred to as Zheda, is a national university in China.  Founded in 1897, Zhejiang University is one of China's oldest, most selective and most prestigious institutions of higher education.  It is a member of the C9 League, the Yangtze Delta Universities Alliance and the Association of Pacific Rim Universities.

Zhejiang University School of Medicine: Zhejiang University School of Medicine (ZJU Med, Traditional Chinese: 浙江大學醫學院; Simplified Chinese: 浙江大学医学院), is the medical school of Zhejiang University in Hangzhou, Zhejiang Province, People's Republic of China.  It is constantly ranked, as its parent Zhejiang University, among the elite schools in China and Asia.  In 2011, it ranked 4th overall in China.

Zhejiang University Press: Zhejiang University Press (traditional Chinese: 浙江大學出版社; simplified Chinese: 浙江大学出版社) is the official press of Zhejiang University (People's Republic of China).

Journal of Zhejiang University: The Journal of Zhejiang University (Traditional Chinese: 浙江大學學報, Simplified Chinese: 浙江大学学报) is a peer-reviewed academic journal series published by the Zhejiang University Press.  There are eight sub-journals, covering the fields of science, engineering, medicine, humanities, and social sciences.

Zhejiang University Libraries System: Zhejiang University Libraries System or simply Zhejiang University Library or Zheda Library, is the libraries system of Zhejiang University, and one of the largest university libraries in China.

Lanzhou University: Lanzhou University () is a major research university in Lanzhou, Gansu Province, China.  Founded in 1909, it is one of the key universities under China's Ministry of Education (Project 985 & Project 211).  It provides programs for undergraduate, graduate students on four campuses—three in Lanzhou city centre and one in Yuzhong County, about 30 miles away from the main campus.  Total enrolment is approximately 20,000.  Undergraduate students study at the Yuzhong campus.  There are 6 National Bases for the Training of Researching and Teaching personnel for Fundamental Disciplines.  The University operates an additional 35 institutes along with 1 national key Laboratory of the Applied Organic and 3 key laboratories of Arid and Grassland Ecology, West China Environment, Magnetism and Magnetic Materials of the Ministry of Education, a key laboratory of Grassland Agro-ecosystem of the Ministry of Agriculture.  Lanzhou University was one of the first universities entitled to enroll Bachelor Master’s and Doctoral degree candidates in 1981.  Lanzhou University is one of the top ten universities in contributions to academic publications in international journals frequently cited by ongoing research from around the world.

Question: How many universities are included with Zhejiang University in the official alliance which produces 20% of the nations academic publications and 30% of total citations in China?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "alliance_name": {
      "type": "string",
      "description": "The name of the official alliance."
    },
    "total_universities_in_alliance": {
      "type": "integer",
      "description": "The total number of universities in the alliance."
    },
    "zhejiang_university_is_member": {
      "type": "boolean",
      "description": "Indicates if Zhejiang University is a member of this alliance."
    },
    "academic_publications_percentage": {
      "type": "integer",
      "description": "The percentage of the nation's academic publications produced by the alliance."
    },
    "total_citations_percentage": {
      "type": "integer",
      "description": "The percentage of total citations accounted for by the alliance."
    }
  },
  "required": [
    "alliance_name",
    "total_universities_in_alliance",
    "zhejiang_university_is_member",
    "academic_publications_percentage",
    "total_citations_percentage"
  ],
  "additionalProperties": false
}
