submission = pd.DataFrame({
"PARENT_JOB":list(test["PARENT_JOB"]),
"BUCKET_Number":list(X_test["BUCKET_NAME"]),
"y_actual":list(y_test),
"y_pred":list(y_pred),
"probabilities":list(pred),
"duration": list(test["DURATION"])
})


submission['probabilities'] = [p[1] for p in pred]
submission = submission.sort_values(by=['probabilities'], ascending=False)
print("Prioritized Test Cases with Durations:")
print(submission[['PARENT_JOB', 'y_pred', 'probabilities', 'duration']])
# Save the submission DataFrame to a CSV file
submission.to_csv(f'test_case_durations_{clf.__class__.__name__}.csv', index=False)