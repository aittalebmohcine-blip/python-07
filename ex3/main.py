from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main() -> None:
    print("=== DataDeck Game Engine ===")

    print("\nConfiguring Fantasy Card Game...")
    engine = GameEngine()
    factory = FantasyCardFactory()
    try:
        strategy = AggressiveStrategy("AggressiveStrategy")
    except TypeError as e:
        strategy = None
        print(e)

    try:
        engine.configure_engine(factory, strategy)
        print(f"Factory: {engine.factory.__class__.__name__}")
        print(f"Strategy: {engine.strategy.__class__.__name__}")
        print(f"Available types: {engine.factory.get_supported_types()}")

        print("\nSimulating aggressive turn...")
        result = engine.simulate_turn()
        hand = ", ".join(
            [f"{card.name} ({card.cost})" for card in engine.hand]
        )
        print(f"Hand: [{hand}]")

        print("\nTurn execution:")
        print(f"Strategy: {engine.strategy.get_strategy_name()}")
        print(f"Actions: {result}")

        print("\nGame Report:")
        print(engine.get_engine_status())
    except Exception as e:
        print(e)

    print(
        "\nAbstract Factory + Strategy "
        "Pattern: Maximum flexibility achieved!"
        )


if __name__ == "__main__":
    main()
