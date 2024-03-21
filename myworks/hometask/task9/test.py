from v1 import main as main1
from v2 import main as main2


def test(main):
    print(main("{ <section> declare #-5759 -> @'riquso'. </section>. <section>declare"
               "#1855 ->@'ceus_935'.</section>. <section>declare#-8566 ->@'quve_443'.</section>.}"))
    print(main(
        "{ <section> declare#-6210 -> @'orardi_12'. </section>. <section>declare #-8722 -> @'leis_589'. "
        "</section>. <section> declare #1561 ->@'ramaus'. </section>. <section> declare #-5276 -> @'tima'.</section>.}"))


if __name__ == '__main__':
    test(main1)
    test(main2)
