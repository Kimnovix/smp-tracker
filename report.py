from tracker import analyze_day

if __name__ == "__main__":
    # Execute the predictive pipeline
    result = analyze_day(sleep_hr=7.5, water_glasses=9, bench_kg=88)
    
    # Output the results
    print(f"Prediction: {'HIT GOAL' if result['hit_goal'] else 'MISS GOAL'} ({result['confidence']:.2%} confidence)")
    print(f"Coach: {result['coaching']}")