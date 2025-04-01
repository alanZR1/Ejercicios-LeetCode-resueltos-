# mi solucion 
class Solution(object):
    def maximumLength(self, s: str) -> int:
        n = len(s)
        # Iterar sobre las longitudes posibles, desde la mayor hasta la menor
        for longitud in range(n, 0, -1):
            conteo = {}
            # Desplazar una ventana de tamaño `longitud` sobre la cadena
            for i in range(n - longitud + 1):
                sub = s[i:i+longitud]
                # Verificar si la subcadena es especial (todos los caracteres son iguales)
                if len(set(sub)) == 1:
                    # Contar las ocurrencias usando un diccionario
                    conteo[sub] = conteo.get(sub, 0) + 1
                    # Si aparece al menos 3 veces, devolver la longitud
                    if conteo[sub] >= 3:
                        return longitud
        return -1  # Si no encontramos ninguna subcadena válida, devolvemos -1


# Crear un objeto de la clase Solution y usarlo
finder = Solution()

# imprimir aplicando metodos 'def'
print(finder.maximumLength("aaaa"))   # Salida: 2
print(finder.maximumLength("abcdef")) # Salida: -1
print(finder.maximumLength("abcaba")) # Salida: 1



#solucion mas usada :

from collections import Counter
class Solution(object):
    def maximumLength(self, s):
        if len(set(s))==1:
            return len(s)-2
        k=Counter(s)
        if max(k.values())<3:
            return -1
        frq = self.findhue(s)
        l = 0
        r = len(s)
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if self.ispossible(mid, frq):
                ans = mid  
                l = mid + 1  
            else:
                r = mid - 1  
        return ans if ans != -1 else -1
    
    def ispossible(self, mid, frq):
        count = 0
        for counts in frq.values():
            for j in counts:
                count += max(0, j - mid + 1)  
            if count >= 3:  
                return True
            count=0
        return False

    def findhue(self,s):
        freq={}
        l=0
        count=0
        for r in range(len(s)):
            if s[r]==s[l]:
                count+=1
            else:
                if s[l] in freq:
                    freq[s[l]].append(count)
                    l=r
                    count=1
                else:
                    freq[s[l]]=[count]
                    l=r
                    count=1
        if s[l] in freq:
            freq[s[l]].append(count)
        else:
            freq[s[l]]=[count]
        return freq
sol=Solution()
s="abcccccdddd"
print(sol.maximumLength(s))


#solucion mas optima:

class Solution(object):
    def maximumLength(self, s):
        
        import heapq
        res = -1
        dic = {}
        l = 0
        for i, c in enumerate(s):
            if c not in dic:
                dic[c] = []
                heapq.heapify(dic[c])
            if c != s[l]:
                ml = i - l
                heapq.heappush(dic[s[l]], ml)
                if len(dic[s[l]]) > 3:
                    heapq.heappop(dic[s[l]])
                l = i
        ml = len(s) - l
        heapq.heappush(dic[s[l]], ml)
        if len(dic[s[-1]]) > 3:
            heapq.heappop(dic[s[-1]])
        for c in dic:
            arr = dic[c]
            arr.sort(reverse=True)
            res = max(res, arr[0] - 2)
            if len(arr) > 2:
                if arr[0] == arr[1] and arr[1] == arr[2]:
                    res = max(res, arr[0])
                if arr[0] > arr[1]:
                    res = max(res, arr[1])
                else:
                    res = max(res, arr[1] - 1)
            elif len(arr) == 2:
                if arr[0] > arr[1]:
                    res = max(res, arr[1])
                else:
                    
                    res = max(res, arr[1] - 1)
        return res if res > 0 else -1