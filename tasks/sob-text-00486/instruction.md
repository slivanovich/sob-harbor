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
Presidency of Bill Clinton: The presidency of Bill Clinton began at noon EST on January 20, 1993, when Bill Clinton was inaugurated as President of the United States, and ended on January 20, 2001.  Clinton, a Democrat, took office as the 42nd United States president following a decisive victory over Republican incumbent president George H. W. Bush and Independent businessman Ross Perot in the 1992 presidential election.  Four years later, in the 1996 election, he defeated Perot and Republican Bob Dole to win re-election.  During both elections, Clinton ran as a New Democrat, and many of his administration's policy proposals reflected his centrist, Third Way thinking.  He was the first president elected after the end of the Cold War, the first Baby Boomer to become president, and also the first Democrat since Franklin D. Roosevelt to serve two full terms.  He was succeeded by Republican George W. Bush, who won the 2000 presidential election.

Bill Ramsey (singer): William McGreery Ramsey, called Bill, was the son of a teacher and an advertising manager for " Procter & Gamble ".  In his youth, he sang in a college dance band.  He began to study sociology and business from 1949 to 1951 at Yale university in New Haven and sang jazz, Swing and Blues in the evenings.  His greatest influences were Count Basie, Nat King Cole, Duke Ellington and Louis Jordan.  Due to the Korean War, compulsory military service was again introduced in the USA and Bill Ramsey served with the U.S. Air Force in Germany.  During this time period, he appeared in clubs like " Jazz Cellar " in Frankfurt/Main and was discovered by an employee of AFN and hired to entertain troops.  There Ramsey advanced to executive producer and had, although still in service, more time for appearances at festivals.  As of 1953, he appeared with, among others, Ernst Mosch, Paul Kuhn, Kurt Edelhagen and James Last.  The jazz pianist and music producer Heinz Gietz organized an appearance with Hessischer Rundfunk for Bill Ramsey in 1955.  There he did Playback – recordings for the musical film "love, dance and 1000 hits" with Peter Alexander and Caterina Valente.  Upon his discharge from the military he continued his studies in America and returned to Frankfurt in 1957.

Impeachment of Bill Clinton: The impeachment process of Bill Clinton was initiated by the House of Representatives on December 19, 1998, against Bill Clinton, the 42nd President of the United States, on two charges, one of perjury and one of obstruction of justice.  These charges stemmed from a sexual harassment lawsuit filed against Clinton by Paula Jones.  Clinton was subsequently acquitted of these charges by the Senate on February 12, 1999.  Two other impeachment articles – a second perjury charge and a charge of abuse of power – failed in the House.

Craig T. Smith: He was described by "TIME" magazine as "something of an adopted son" to President Bill Clinton and Hillary Clinton.  He was the first hire of President Bill Clinton's successful campaign during the 1992 election.  He began working for President Clinton while the later was governor of Arkansas.

First inauguration of Bill Clinton: The first inauguration of Bill Clinton as the 42nd President of the United States was held on Wednesday, January 20, 1993 on the West Front of the United States Capitol Building in Washington, D.C..  The inauguration marked the commencement of the first four-year term of Bill Clinton as President and Al Gore as Vice President.  At of age time of his first inauguration, Clinton was the third-youngest person to become president, and the first from the Baby Boomer generation.

Toni Morrison: Toni Morrison (born Chloe Ardelia Wofford; February 18, 1931) is an American novelist, editor, teacher, and professor emerita at Princeton University.

Timeline of the presidency of Bill Clinton: The presidency of Bill Clinton began on January 20, 1993 at noon Eastern Standard Time, when Bill Clinton was inaugurated as President of the United States, and ended on January 20, 2001.  Clinton, a Democrat, took office after defeating Republican incumbent President George H. W. Bush and Independent businessman Ross Perot in the 1992 presidential election.  Four years later, he defeated Republican Bob Dole and Ross Perot (this time running on the Reform Party ticket) to win a second term of office.  During both elections, Clinton ran as a New Democrat, and many of many of his administration's policy proposals reflected his centrist, Third Way thinking.  The 42nd United States president, he was the first president elected after the end of the Cold War, the first Baby Boomer to become president, and also the first Democrat since Franklin D. Roosevelt to serve two full terms.

Vast right-wing conspiracy: "Vast right-wing conspiracy" is a conspiracy theory first described in a 1995 memo by political opposition researcher Chris Lehane and then referenced in 1998 by the then First Lady of the United States Hillary Clinton, in defense of her husband, President Bill Clinton, characterizing the continued allegations of scandal against her and her husband, including the Lewinsky scandal, as part of a long campaign by Clinton's political enemies.  The term has been used since, including in a question posed to Bill Clinton in 2009 to describe verbal attacks on Barack Obama during his early presidency.  Hillary Clinton mentioned it again during her 2016 presidential campaign.

Hospital, patients, health, territories: Hospital, patients, health, territories is the official name of a French bill presented on 22 October 2008 by Roselyne Bachelot, minister of Health, Youth, Sports and Associative Life.  The bill is commonly called bill HPST (acronym of the French phrase) or bill Bachelot.  The bill is the first stage of the Hospital 2012 Plan, launched by French President Nicolas Sarkozy, which aims at revamping of the French health care system.  The bill aims at guarantee a better and equal access to care for all French people, whatever their geographic location.  This reform needs a complete overhaul of the hospitals organization, which caused strong protests among the staffs.

Public image of Bill Clinton: Former U.S. President Bill Clinton's public image is most notably characterized by high public approval ratings, aided by his youthful appearance, as well as his charismatic, and soundbite-ready style of speech.  His personal background and lifestyle led to Nobel Prize-winning novelist Toni Morrison to call him the first "black president".  Clinton was also dogged by investigations throughout his presidency, particularly of sexual misconduct, damaging the public's beliefs of his trustworthiness, though his approval ratings remained high, even as his impeachment trial continued.

Question: At which University is the novelist who called Bill Clinton the first "black president" a professor ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "novelist_name": {
      "type": "string",
      "description": "The name of the novelist."
    },
    "university_name": {
      "type": "string",
      "description": "The name of the university where the novelist is a professor."
    },
    "professor_status": {
      "type": "string",
      "description": "The specific status or title of the novelist at the university (e.g., professor emerita)."
    },
    "quote_about_clinton": {
      "type": "string",
      "description": "The quote attributed to the novelist regarding Bill Clinton."
    }
  },
  "required": [
    "novelist_name",
    "university_name",
    "professor_status",
    "quote_about_clinton"
  ],
  "additionalProperties": false
}
