"use client";

import { useState } from "react";

export default function Term() {
  const [cmd, setCmd] = useState("");
  const [history, setHistory] = useState([]);

  const handSubmit = (e) => {
    e.preventDefault();

    switch (cmd) {
      case "hello":
        setHistory([...history, { cmd, response: "hi!!" }]);
        break;
      case "bye":
        setHistory([...history, { cmd, response: "bye!!" }]);
        break;
      default:
        setHistory([...history, { cmd, response: "Command does not exists" }]);
        break;
    }
    setCmd("");
  };
  return (
    <>
      <div className="fixed top-52 right-0 left-0 mx-60">
        <div className="bg-gray-400 rounded-t-lg flex items-center px-2 py-1">
          <div className="flex justify-evenly gap-2">
            <div className="rounded-3xl bg-red-500 p-[6px]"></div>
            <div className="rounded-3xl bg-yellow-500 p-[6px]"></div>
            <div className="rounded-3xl bg-green-500 p-[6px]"></div>
          </div>
          <div className="text-center flex-grow">Helo</div>
        </div>
        <div className="scroll h-80 rounded-b-lg backdrop-blur-sm bg-gray-800 bg-opacity-50 px-2 py-1 overflow-y-scroll">
          <div>
            {history.map(({ cmd, response }, idx) => (
              <div key={idx}>
                <div className="text-green-300 font-bold">
                  ~ -&gt; <span className="text-white font-normal">{cmd}</span>
                </div>
                <div className="text-white">{response}</div>
              </div>
            ))}
          </div>
          <div className="bg-transparent flex gap-1">
            <div className="text-green-300 font-bold">~ -&gt;</div>
            <form onSubmit={(e) => handSubmit(e)} className="flex-grow">
              <input
                type="text"
                name=""
                id=""
                maxLength={114}
                className="bg-transparent outline-none text-white w-full"
                value={cmd}
                onChange={(e) => setCmd(e.target.value)}
              />
            </form>
          </div>
        </div>
      </div>
      <div>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatum
        natus quasi soluta nam veritatis sunt at reiciendis, beatae quia quod,
        ducimus repellendus placeat velit. Velit consequatur beatae nisi enim
        accusamus. Magni, assumenda velit. Recusandae hic deleniti
        necessitatibus in veniam id rem cupiditate sint, voluptas deserunt quo,
        eius sed ducimus tempore nemo obcaecati? Dolor officia dolorum tempora
        animi tempore minima blanditiis! Quis maiores iusto corporis eos odit.
        Nam vero minus doloremque magni delectus nobis eaque, ipsum eligendi
        sequi dicta atque aspernatur blanditiis ab quisquam dignissimos?
        Repellat ab atque nihil voluptatum aliquam. Consectetur nobis rerum
        fugiat, aperiam iste error placeat voluptas alias perferendis, est magni
        dolorem praesentium suscipit non, nihil quasi corrupti ipsum quam
        voluptate porro blanditiis velit laborum saepe. Accusantium, dolores?
        Architecto totam quae modi fugiat repellat rem ea, beatae voluptatibus
        enim, debitis animi, amet magnam doloremque blanditiis dolorem
        laudantium minus distinctio eius reiciendis accusamus laborum.
        Provident, maxime delectus. Perferendis, ad. Iste consectetur magni
        natus perferendis accusamus pariatur aliquam exercitationem corrupti
        recusandae vel, veniam assumenda repellat aperiam magnam expedita
        aspernatur perspiciatis labore nemo optio maiores illum deserunt unde
        error! Non, vero. Pariatur temporibus, cumque modi error accusamus
        placeat ratione doloribus sed doloremque quisquam repellendus quas
        voluptas nobis ab, ex laudantium, consequuntur impedit praesentium? Enim
        excepturi soluta ullam consequatur fuga sed libero? Dolorem sed dicta
        sequi ipsa, mollitia porro impedit excepturi optio beatae perspiciatis
        adipisci deserunt. Explicabo, fugiat! Voluptate, dolorem. Totam laborum
        corporis sint alias libero dicta rem corrupti nobis minus. Impedit. Vero
        laboriosam sint repellendus neque totam accusantium nobis cum laborum
        voluptates voluptate quasi perferendis dolore optio est hic pariatur,
        exercitationem mollitia quam. Ratione expedita minima error repellat,
        pariatur iure nemo. Nostrum deserunt qui, officia voluptate odit
        recusandae autem cum sit nihil reprehenderit sapiente vel totam
        laboriosam magnam hic, minus quasi necessitatibus quibusdam iste!
        Eligendi cum ad excepturi inventore corporis quae.
        <br />
        <br />
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quo
        consectetur distinctio ipsum quis cupiditate expedita ab quam libero,
        nesciunt ipsam dolore! Quod possimus earum reprehenderit vero illum
        repellendus sequi molestias. Molestias molestiae id minus, suscipit fuga
        nemo incidunt ex, ipsum possimus omnis minima quisquam, ipsa culpa hic!
        Iure dolore culpa reprehenderit magnam eaque, eum quam minima minus, at
        illum amet? Nobis tempore minus illo praesentium fuga inventore deserunt
        veniam sapiente. Vero, ab ex tenetur labore deleniti porro quod,
        temporibus fugit architecto voluptatem iure ratione deserunt quos
        maxime, amet a pariatur! Ea ratione explicabo, delectus laudantium
        accusamus, et error debitis iure saepe qui consectetur excepturi, quis
        odio harum fugiat impedit! Impedit officiis sequi cum harum. Sapiente
        reiciendis consequatur nisi odio a. Odit, sapiente aliquid vero, ipsa
        quas unde aliquam nobis et suscipit ea iusto facere maiores, placeat
        consequuntur deleniti. Necessitatibus rerum dolore laudantium doloribus
        deserunt rem officiis quia id quas illo.
        <br />
        <br />
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Aperiam et
        velit magnam, ad repudiandae molestias ullam ea dolorum mollitia
        aspernatur enim officiis soluta accusamus deleniti vitae quos dolore in
        non? Nostrum nihil reprehenderit mollitia totam sed vel nisi perferendis
        exercitationem, voluptatum provident distinctio animi cum architecto
        placeat suscipit voluptates consequuntur ipsam, amet excepturi tenetur
        ex. Repudiandae, eius? Suscipit, enim exercitationem? Esse animi
        perspiciatis nostrum exercitationem. Odit animi natus iste. Totam
        voluptas quas odio reprehenderit provident laborum? Voluptate, id amet
        atque ipsam enim rerum et repellat voluptates. Pariatur sit amet dolore!
        Hic, vel beatae modi ut ex temporibus officiis ipsa rem incidunt
        voluptatibus ratione consequuntur autem, libero a vitae nostrum
        aspernatur earum facilis! Explicabo beatae quos alias similique quae!
        Ad, expedita. Odit, commodi. Sed tempore nisi reiciendis assumenda vel
        facere illum perferendis, nobis rerum dolorem alias quos possimus! Quos
        enim alias, cum soluta qui, voluptatem sunt numquam, est deserunt
        ducimus ipsam? Quasi tempora aliquam molestiae. Quae deserunt nesciunt
        nostrum in aperiam suscipit fuga quibusdam tempora accusantium
        temporibus unde, expedita, maiores sunt esse incidunt optio velit beatae
        soluta, repudiandae omnis laboriosam rem. Odio ipsum error inventore,
        aperiam fugit sequi voluptatem. Corrupti ullam, facere fugit quos neque
        aliquid pariatur temporibus voluptates amet vero sed possimus modi
        doloribus nulla optio consequuntur itaque! Culpa, numquam.
        Exercitationem deleniti similique inventore nemo, vitae iusto vero
        aliquid et aut accusantium assumenda fugiat culpa eius numquam
        voluptatum nesciunt corporis blanditiis. Dolor architecto recusandae
        tempore ab praesentium laborum delectus ea. Iure accusamus libero
        consequatur ex consectetur temporibus reiciendis atque ea similique,
        sint inventore facilis nobis tempore nam ratione debitis soluta omnis
        optio recusandae, fugit quaerat quis deserunt. Consequatur, nisi
        repudiandae. Omnis non id nostrum eum culpa ipsum exercitationem quod
        dolorem, illum est accusamus tenetur obcaecati repudiandae sit vel
        adipisci, architecto saepe quae labore fugiat. A cumque deleniti error
        illum nesciunt? Dicta iusto dignissimos minima molestias cumque tenetur.
        Ducimus ut veniam neque accusamus, praesentium cum aperiam ipsum
        deserunt, dolores eos, fugiat mollitia qui et. Praesentium cum
        reiciendis deserunt maxime, at eius. Aspernatur corporis assumenda
        fugiat vel autem, commodi expedita, asperiores, incidunt possimus nam
        quis alias deserunt exercitationem aperiam. Sunt sequi vero distinctio,
        dignissimos atque, impedit ea nemo quas, amet dolore perspiciatis. Error
        sapiente provident molestiae veritatis nemo, modi dolorum quidem quas
        est, quo tempore eum magni totam aspernatur rem ratione quia? Corporis
        veritatis numquam distinctio suscipit ducimus vel quod reiciendis odit.
        Blanditiis provident similique corrupti ullam incidunt. Similique
        facilis saepe error nulla aut corporis a quasi ratione eius laudantium
        sed tempore facere, vel nihil magnam ipsam consequuntur. Nobis sed vero
        architecto? Neque quibusdam cupiditate ipsum ab consectetur voluptas
        laudantium laborum officiis doloribus. Eos modi cum cupiditate aperiam,
        molestias aliquam, atque blanditiis quia architecto velit dolorem error
        hic, perspiciatis vero doloribus nihil?
      </div>
    </>
  );
}
