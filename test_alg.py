import time
import tracemalloc
import pandas as pd

def universal_test_system(solutions_dict, test_cases_dict):

    all_results = []
    
    for task_name, solution_func in solutions_dict.items():
        test_cases = test_cases_dict.get(task_name, [])
        
        print(f"\n{'='*60}")
        print(f"📊 ТЕСТИРОВАНИЕ: {task_name}")
        print(f"{'='*60}")
            
        for i, test_case in enumerate(test_cases, 1):
            print(f"Запуск теста {i}...")
            
            input_data = test_case.get('input', test_case)
            expected = test_case.get('expected')
            
            result = None
            execution_time = 0
            memory_mb = 0
            correctness = 'ERROR'
            error_msg = None
            
            try:
                tracemalloc.start()
                start_time = time.time()
                
                if isinstance(input_data, (list, tuple)):
                    result = solution_func(*input_data)
                elif isinstance(input_data, dict):
                    result = solution_func(**input_data)
                else:
                    result = solution_func(input_data)
                
                execution_time = (time.time() - start_time) * 1000
                current, peak_memory = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                memory_mb = peak_memory / 1024 / 1024
                
                correctness = '✓' if result == expected else '✗'
                error_msg = None
                
            except Exception as e:
                tracemalloc.stop()
                execution_time = (time.time() - start_time) * 1000
                error_msg = f"{type(e).__name__}: {str(e)}"
                correctness = 'ERROR'
                print(f"   Ошибка в тесте {i}: {error_msg}")
            
            test_result = {
                'Задача': task_name,
                'Тест': i,
                'Входные данные': str(input_data)[:50],
                'Ожидаемый результат': str(expected)[:30],
                'Полученный результат': str(result)[:30] if result is not None else "None",
                'Корректность': correctness,
                'Время (мс)': f"{execution_time:.2f}",
                'Память (Мб)': f"{memory_mb:.4f}",
                'Ошибка': error_msg
            }
            
            all_results.append(test_result)
            
            status_icon = '✓' if correctness == '✓' else '✗' if correctness == '✗' else '💥'
            print(f"Тест {i}: {status_icon} | Время: {execution_time:.2f}мс | Память: {memory_mb:.4f}Мб")
    
    print(f"\n{'='*80}")
    print("📋 СВОДНАЯ ТАБЛИЦА РЕЗУЛЬТАТОВ")
    print(f"{'='*80}")
    
    if all_results:
        df = pd.DataFrame(all_results)
        
        display_columns = ['Тест', 'Входные данные', 
                          'Ожидаемый результат', 'Полученный результат', 'Время (мс)', 'Память (Мб)']
        
        available_columns = [col for col in display_columns if col in df.columns]
        
        if available_columns:
            print(df[available_columns].to_string(index=False, max_colwidth=25))
        else:
            print("Нет данных для отображения")
        
        return df
    else:
        return pd.DataFrame()