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
UkrTransNafta: UkrTransNafta (Ukrainian: "УкрТрансНафта" ) is an open joint-stock company established by the government of Ukraine in June 2001.  The company exists to manage oil transportation operations through the Ukrainian pipeline network.  The company oversees the activities of two main oil pipeline systems: the Ukrainian section of the Druzhba pipeline, and the Pridniprovski oil pipeline.  The company is also in charge of the Odessa-Brody pipeline.

Mosul–Haifa oil pipeline: The Mosul–Haifa oil pipeline (also known as the Iraq–Haifa pipeline or Mediterranean pipeline) was a crude oil pipeline from the oil fields in Kirkuk, located in the former Ottoman vilayet of Mosul in northern Iraq, through Jordan to Haifa (in mandatory Palestine, now in the territory of Israel).  The pipeline was operational between 1935 and 1948.  Its length was about 942 km , with a diameter of 12 in (reducing to 10 and in parts), and it took about 10 days for crude oil to travel the full length of the line.  The oil arriving in Haifa was distilled in the Haifa refineries, stored in tanks, and then put in tankers for shipment to Europe.

Indian Oil Corporation: Indian Oil Corporation Limited (IOCL) (, ), commonly known as IndianOil is an Indian oil and gas company headquartered in Mumbai.  It is the largest commercial enterprise in the country, with a net profit of INR 19,106 crore (USD 2,848 million) for the financial year 2016–17.  It is ranked 1st in Fortune India 500 list for year 2016 and 168th in Fortune's ‘Global 500’ list of world's largest companies in the year 2017.  As of 31st March, 2017 IndianOil's employee strength is 33,135, out of which 16,545 are in the officer cadre.

Druzhba pipeline: The Druzhba pipeline (Russian: нефтепровод «Дружба» ; also has been referred to as the Friendship Pipeline and the Comecon Pipeline) is the world's longest oil pipeline and in fact one of the biggest oil pipeline networks in the world.  It carries oil some 4000 km from the eastern part of the European Russia to points in Ukraine, Belarus, Poland, Hungary, Slovakia, the Czech Republic and Germany.  The network also branches out into numerous pipelines to deliver its product throughout Eastern Europe and beyond.  The name "Druzhba" means "friendship", alluding to the fact that the pipeline supplied oil to the energy-hungry western regions of the Soviet Union, to its "fraternal socialist allies" in the former Soviet bloc, and to western Europe.  Today, it is the largest principal artery for the transportation of Russian (and Kazakh) oil across Europe.

Keystone Pipeline: The Keystone Pipeline System is an oil pipeline system in Canada and the United States, commissioned in 2010 and now owned solely by TransCanada Corporation.  It runs from the Western Canadian Sedimentary Basin in Alberta to refineries in Illinois and Texas, and also to oil tank farms and an oil pipeline distribution center in Cushing, Oklahoma.  The pipeline came to a greater prominence of attention when a planned fourth phase, Keystone XL, attracting growing environmental protest, became a symbol of the battle over climate change and fossil fuels, and in 2015 was rejected by then President Barack Obama.  On January 24, 2017, President Donald Trump took action intended to permit the pipeline's completion.

Lanzhou–Chengdu Pipeline: The Lanzhou–Chengdu Pipeline is a crude oil pipeline in China.  Connected to the Ürümqi–Lanzhou pipeline, it transports crude oil produced in Xinjiang as also imported through the Kazakhstan–China oil pipeline to south-western China.  Among other customers it supplies the Pengzhou refinery.  The pipeline is owned by China National Petroleum Corporation.

2010 Puebla oil pipeline explosion: The 2010 Puebla oil pipeline explosion was a large oil pipeline explosion that occurred at 5:50 am CST on December 19, 2010, in the city of San Martín Texmelucan de Labastida, Puebla, Mexico.  The pipeline, running from Tabasco to Hidalgo, was owned by the Pemex petroleum company, and exploded after thieves from the Los Zetas drug cartel attempted to siphon off the oil.  The gas explosion and resulting oil fire killed 29 people, including thirteen children, and injured 52.  Some of the flames in the fire became ten metres high, and the smoke towered over the city.  The blast also damaged 115 homes, completely destroying 32 of them, and prompted the evacuation of 5,000 residents.  Firefighters eventually controlled the blaze, but electricity and water remained cut following the explosions, and the military was deployed to the site.  Mexican President Felipe Calderón visited the explosion site on the day of the incident to offer condolences to the victims' families.  The fire was one of the deadliest in Mexican history, largely destroying an area of five-kilometre radius, and some oil may have polluted the Atoyac River.

Kenya Crude Oil Pipeline: Kenya Crude Oil Pipeline, also Lokichar–Lamu Crude Oil Pipeline, is a proposed crude-oil pipeline in Kenya.  The pipeline will originate in the oil-rich South Lokichar Basin, near the town of Lokichar, in northwest Kenya to end at Port Lamu, on the Indian Ocean.  The route will remain as originally planned in the Uganda–Kenya Crude Oil Pipeline, in August 2015.  The route, was proposed by Toyota Tsusho, the consultant selected by the two governments of that now-abandoned project.

Kandla–Bhatinda Oil Pipeline: Kandla–Bhatinda Oil Pipeline (KBPL) was started in 1993 and it was commissioned in 1996.  It is the largest oil pipeline of India.  However, the first engineering firm to work on the project, Škoda Export, did not complete the job and fresh bids had to be taken in 1996.  The total length is 1443 km with a capacity of 6.0 MMTPA.  It was recommissioned later the same year.  The pipeline transports oil brought into India to consumers of North India which is land locked.  The pipeline is owned by Indian Oil Corporation.  Initially, it was a product pipeline.  Now it is a crude oil pipeline from Kandla to Panipat and subsequently it is a product pipeline up to Bhatinda.

Odessa–Brody pipeline: The Odessa–Brody pipeline (also known as Sarmatia pipeline) is a crude oil pipeline between the Ukrainian cities Odessa at the Black Sea, and Brody near the Ukrainian-Polish border.  There are plans to expand the pipeline to Płock, and furthermore to Gdańsk in Poland.  The pipeline is operated by UkrTransNafta, Ukraine's state-owned oil pipeline company.

Question: The Kandla–Bhatinda Oil Pipeline is owned by a company headquartered in what city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "pipeline_name": {
      "type": "string",
      "description": "The name of the oil pipeline."
    },
    "owner_company": {
      "type": "string",
      "description": "The name of the company that owns the pipeline."
    },
    "owner_company_headquarters_city": {
      "type": "string",
      "description": "The city where the owner company is headquartered."
    }
  },
  "required": [
    "pipeline_name",
    "owner_company",
    "owner_company_headquarters_city"
  ],
  "additionalProperties": false
}
