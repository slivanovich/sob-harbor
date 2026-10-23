{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLakheri: Lakheri ( ) is a town with municipality in Bundi district in the Indian state of Rajasthan. It is located in southeast northern Indian state of Rajasthan.  It is located Around 180 km south of the state capital, Jaipur.  Lakheri is subdivision headquarter since 2002.  Mamta kumari tiwari (RAS) is deputy Collector & Majistrate of lakheri subdivision.  This is the second largest city after Bundi in the district.\n\nKerala: Kerala ( ), historically known as Keralam, is an Indian state in South India on the Malabar Coast.  It was formed on 1 November 1956 following the States Reorganisation Act by combining Malayalam-speaking regions.  Spread over 38863 km2 , it is bordered by Karnataka to the north and northeast, Tamil Nadu to the east and south, and the Lakshadweep Sea to the west.  With 33,387,677 inhabitants as per the 2011 Census, Kerala is the thirteenth-largest Indian state by population.  It is divided into 14 districts with the capital and the largest city being Thiruvananthapuram.  Malayalam is the most widely spoken language and is also the official language of the state.\n\nBengali Hindus: Bengali Hindus (Bengali: বাঙালি হিন্দু ) are ethnic Bengali adherents of Hinduism, and are native to the Bengal region of the Indian subcontinent.  Bengali Hindus speak Bengali, which belongs to the Indo-Aryan language family and adhere to the Shakta and Vaishnava traditions of their native religion, Hinduism.  The Bengali Hindu population is mainly concentrated in the Indian state of West Bengal where they are majority (70.54%) and it is also called the Bengali Hindu homeland which is created on the time of partition of India to ensure a safe homeland for Bengali Hindus in the Bengal region of Indian subcontinent by Shyama Prasad Mukherjee, and in Bangladesh, they are the second-largest group just after Bengali Muslims.  Bengali Hindus also form a majority of 60% in the Indian state of Tripura, due to mass migrations from East Pakistan and Bangladesh in the latter half of the 20th century.  There are significant numbers of Bengali-speaking Hindus in many states of India, including Assam, Karnataka (especially in the capital of Bangalore), Meghalaya, Jharkhand, Odisha, and the Union Territory of Andaman and Nicobar Islands.  There is also a diaspora.\n\nTundla Railway Colony: Tundla Railway Colony is a census town in Firozabad district in the Indian state of Uttar Pradesh.\n\nMaitree Express: The Maitree Express (Hindi: मैत्री एक्सप्रेस ), or Moitree Express (Bengali: মৈত্রী এক্সপ্রেস ), is the name of international passenger train servies connecting Bangladesh to the Indian state of West Bengal.  The name \"Maitree Express\" means the \"Friendship Express\", denoting the significance of the train service to the foreign relations between India and Bangladesh.  Train services between the two countries existed before the partition of India – the \"Maitree Express\" re-established this connection between the Bangladeshi capital of Dhaka with Kolkata, the capital of the Indian state of West Bengal, in 2008 after being closed for 43 years.  In 2017, a second train (the \"Maitree Express-II\") was inaugurated connecting Kolkata with the Bangladeshi city of Khulna, recreating the previous Barisal Express route.\n\nAgra: Agra ( ; \"Āgrā\") is a city on the banks of the river Yamuna in the northern state of Uttar Pradesh, India.  It is 378 km west of the state capital, Lucknow, 206 km south of the national capital New Delhi and\n\nDelhi–Kolkata high-speed rail corridor: Delhi–Kolkata high-speed rail corridor is one of the route of the proposed high-speed rail in India.  The line is part of the Diamond Quadrilateral Program, which seeks to unite the cities of New Delhi, Kolkata, Mumbai and Chennai via high speed rail.  This travels along the Delhi–Howrah main line from Tundla to Howrah.  The train expects to cut the journey time for the 1500 km between the national capital of India, New Delhi, and the capital of the Indian state of West Bengal, the city of Kolkata, to just 5 hours 30 minutes.\n\nTundla: Tundla is a town and a municipal board in Firozabad district in the Indian state of Uttar Pradesh.  It is located 24 km away from the city of Agra.\n\nHowrah - Bhopal Weekly Express: Bhopal–Howrah Express is a weekly express train of the Indian Railways, which runs between Bhopal Junction railway station of Bhopal, the capital city of Central Indian state Madhya Pradesh and Howrah Junction railway station of Kolkata, the capital city of east Indian state West Bengal.\n\nTundla Kham: Tundla Kham is a census town in Firozabad district in the Indian state of Uttar Pradesh.\n\nQuestion: What is the capital of the Indian state Tundla is located in?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"state_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Indian state where the town is located.\"\n    },\n    \"state_capital\": {\n      \"type\": \"string\",\n      \"description\": \"The capital city of the identified Indian state.\"\n    },\n    \"town_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the town in question.\"\n    }\n  },\n  \"required\": [\n    \"state_name\",\n    \"state_capital\",\n    \"town_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "state_name": {
        "type": "string",
        "description": "The name of the Indian state where the town is located."
      },
      "state_capital": {
        "type": "string",
        "description": "The capital city of the identified Indian state."
      },
      "town_name": {
        "type": "string",
        "description": "The name of the town in question."
      }
    },
    "required": [
      "state_name",
      "state_capital",
      "town_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
