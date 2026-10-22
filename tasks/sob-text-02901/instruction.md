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
Causes of World War I: The causes of World War I remain controversial and debated questions.  The war began in the Balkans in late July 1914 and ended in November 1918, leaving 17 million dead and 20 million wounded.

Centenary of the outbreak of World War I: The centenary of the outbreak of World War I was commemorated in Europe in late July and early August 2014.  A century earlier, the July Crisis, which occurred after the assassination of Archduke Franz Ferdinand, had culminated in Austria-Hungary declaring war on the Kingdom of Serbia, which Austria-Hungary blamed for the assassination, on 28 July 1914.  Over the following days and weeks, this action and the invasion of Luxembourg and Belgium by the German Empire led to a succession of other declarations of war that drew the major European powers into a worldwide conflict.  A century later, governments in Europe held a series of official commemorative events to mark the occasion.

Serbian Campaign of World War I: The Serbian Campaign of World War I was fought from late July 1914, when Austria-Hungary invaded the Kingdom of Serbia at the outset of World War I, until the war's conclusion in November 1918.  The front ranged from the Danube River to southern Macedonia and back north again, and it drew in forces from almost all the combatants of the war.

Serbian Blue Book: The Serbian Blue Book is a collection of 52 Serbian diplomatic documents regarding events between 29 June and 6 August 1914, a period including the aftermath of the assassination of Archduke Ferdinand (the July Crisis) and the beginning of World War I, published by the Government of the Kingdom of Serbia on 18 November 1914.  It includes correspondence between Serbian ministers and diplomats, Serbia and Russia (including royal), Austria-Hungary, and Germany.  It was published in French translation in 1914, and English translation by the British Foreign Office in "Collected Diplomatic Documents Relating to the Outbreak of the European War", and also American Association for International Conciliation, in 1915.

Gavrilo Princip: Gavrilo Princip (Serbian Cyrillic: , ] ; 25 July [O.S. 13 July] 1894 28 April 1918) was a Bosnian Serb member of Young Bosnia, a Yugoslavist organization seeking an end to Austro-Hungarian rule in Bosnia and Herzegovina.  He assassinated Archduke Franz Ferdinand of Austria and his wife, Sophie, in Sarajevo on 28 June 1914, setting off a chain of events that would lead to outbreak of the First World War.  Princip and his accomplices were arrested and implicated the Serbian nationalist secret society known as the Black Hand, leading Austria-Hungary to issue a démarche to Serbia known as the July Ultimatum.  This was used as pretext for Austria-Hungary's invasion of Serbia, which then led to World War I.  Princip was a Yugoslav nationalist associated with the movement Mlada Bosna (Young Bosnia) which predominantly consisted of Serbs, but also Bosniaks and Croats.  During his trial he stated: "I am a Yugoslav nationalist, aiming for the unification of all Yugoslavs, and I do not care what form of state, but it must be freed from Austria."  Princip died on April 28, 1918, from tuberculosis caused by poor prison conditions that had cost him a limb earlier.

List of World War I battles: World War I, which lasted from July 1914 to November 1918 was, at the time, the largest single war ever to have occurred.  There were a large number of allies on each side of the conflict, and their geographical location and that of their imperial provinces meant that parts of the war were fought all over Europe, and in other places such as North Africa, the Middle East, and even minor skirmishes in the Pacific Ocean.  A battle is a smaller conflict between two military enemies that often makes up part of a war.  This is a list (though not exhaustive) of the battles of World War I, in chronological order.  They are organized as to the opening date of the battle.

Battle of Kolubara: The Battle of Kolubara (Serbian: Колубарска битка, "Kolubarska bitka" , German: "Schlacht an der Kolubara" ) was fought between Austria-Hungary and Serbia in November and December 1914, during the Serbian Campaign of World War I.  It commenced on 16 November, when the Austro-Hungarians under the command of Oskar Potiorek reached the Kolubara River during their third invasion of Serbia that year, having captured the strategic town of Valjevo and forced the Serbian Army to undertake a series of retreats.  The Serbs withdrew from Belgrade on 29–30 November, and the city soon fell under Austro-Hungarian control.  On 2 December, the Serbian Army launched a surprise counter-attack all along the front.  Valjevo and Užice were retaken by the Serbs on 8 December and the Austro-Hungarians retreated to Belgrade, which 5th Army commander Liborius Ritter von Frank deemed to be untenable.  The Austro-Hungarians abandoned the city between 14 and 15 December and retreated back into Austria-Hungary, allowing the Serbs to retake their capital the following day.

Sofija Jovanović: Sofija Jovanović (; 1895–1979) was a Serbian war heroine who fought in the Balkan Wars and First World War.  She had joined the Serbian Army under the male name "Sofronije Jovanović" immediately upon the start of World War I and Austria's attack on Serbia.  She defended Belgrade in October 1915 from the armies of Germany and Austria-Hungary.  She was present at the Serbian army's retreat through Albania (winter 1915–16).  She participated at the Salonika Front and the Liberation of Belgrade in November 1918.

List of last World War I veterans by country: This is a list of the last World War I veterans to die by country.  The last living veteran of World War I (28 July 1914 – 11 November 1918) was Florence Green, a British citizen who served in the Allied armed forces, and who died 4 February 2012, aged 110.  The last combat veteran was Claude Choules who served in the British Royal Navy (and later the Royal Australian Navy) and died 5 May 2011, aged 110.  The last veteran who served in the trenches was Harry Patch (British Army) who died on 25 July 2009, aged 111.  The last Central Powers veteran, Franz Künstler of Austria-Hungary, died on 27 May 2008 at the age of 107.

History of Germany during World War I: During World War I, the German Empire was one of the Central Powers that lost the war.  It began participation in the conflict after the declaration of war against Serbia by its ally, Austria-Hungary.  German forces fought the Allies on both the eastern and western fronts, although German territory itself remained relatively safe from widespread invasion for most of the war, except for a brief period in 1914 when East Prussia was invaded.  A tight blockade imposed by the Royal Navy caused severe food shortages in the cities, especially in the winter of 1916–17, known as the Turnip Winter.  At the end of the war, Germany's defeat and widespread popular discontent triggered the German Revolution of 1918–19 which overthrew the monarchy and established the Weimar Republic.

Question: The Battle of Kolubara, was fought between Austria-Hungary and Serbia in November and December 1914, during which campaign of World War I was fought from late July 1914, when Austria-Hungary invaded the Kingdom of Serbia at the outset of World War I, until the war's conclusion in November 1918?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "campaign_name": {
      "type": "string",
      "description": "The name of the World War I campaign."
    },
    "campaign_duration": {
      "type": "object",
      "properties": {
        "start_date": {
          "type": "string",
          "description": "The start date of the campaign."
        },
        "end_date": {
          "type": "string",
          "description": "The end date of the campaign."
        }
      },
      "required": [
        "start_date",
        "end_date"
      ],
      "additionalProperties": false
    },
    "primary_belligerents": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The main countries involved in the campaign."
    },
    "related_battle": {
      "type": "object",
      "properties": {
        "battle_name": {
          "type": "string",
          "description": "The name of the battle mentioned in the context."
        },
        "battle_start_month": {
          "type": "string",
          "description": "The month the battle started."
        },
        "battle_end_month": {
          "type": "string",
          "description": "The month the battle ended."
        },
        "battle_year": {
          "type": "integer",
          "description": "The year the battle took place."
        }
      },
      "required": [
        "battle_name",
        "battle_start_month",
        "battle_end_month",
        "battle_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "campaign_name",
    "campaign_duration",
    "primary_belligerents",
    "related_battle"
  ],
  "additionalProperties": false
}
